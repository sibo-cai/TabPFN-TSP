# Implementation and experiments of TabPFN-TSP, a TabPFN-based time series prediction method
# utilizing the intrinsic periodicity of data
# Author: Sibo Cai
# Last modified：2025-6-13

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datasets import load_dataset
from autogluon.timeseries import TimeSeriesDataFrame
from tabpfn_time_series.data_preparation import to_gluonts_univariate
from tabpfn_time_series.plot import plot_actual_ts

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from tabpfn import TabPFNRegressor


# datasets followed the demo script of TabPFN-TS in Google Colab
# https://colab.research.google.com/github/liam-sbhoo/tabpfn-time-series/blob/main/demo.ipynb
def load_and_save_test_cases(show=True):
    dataset_metadata = {
        "monash_tourism_monthly": {"prediction_length": 24},
        "m4_hourly": {"prediction_length": 48},
    }

    dataset_choice = "monash_tourism_monthly"
    num_time_series_subset = 2

    prediction_length = dataset_metadata[dataset_choice]['prediction_length']
    # dataset = load_dataset("autogluon/chronos_datasets", dataset_choice)
    # load from local disk
    dataset = load_dataset(f"autogluon/chronos_datasets/{dataset_choice}")
    dataset4ts = to_gluonts_univariate(dataset['train'])

    tsdf = TimeSeriesDataFrame(dataset4ts)
    tsdf = tsdf[tsdf.index.get_level_values('item_id').isin(tsdf.item_ids[:num_time_series_subset])]

    groups = tsdf.groupby('item_id')
    for name, group in groups:
        group.to_csv(f'./autogluon/{dataset_choice}_item_{name}.csv', index=False)

    if show:
        train_tsdf, test_tsdf_ground_truth = tsdf.train_test_split(prediction_length=prediction_length)
        plot_actual_ts(train_tsdf, test_tsdf_ground_truth)


def calculate_top_k_periods(csv_file_path, target_column, pred_len, k=1, show=True):
    print("Calculating intrinsic data periodicity using fft...")

    # load csv data
    df = pd.read_csv(csv_file_path)
    data_size = len(df[target_column])

    # remove prediction length
    data_size = data_size - pred_len
    half_data_size = int(data_size / 2)

    history_data = df[target_column][:data_size]
    fft_result = np.fft.fft(history_data)

    frequency_amplitude = np.abs(fft_result)[:half_data_size]
    # exclude frequency 0
    frequency_amplitude[0] = 0

    top_k_frequencies = np.argsort(-frequency_amplitude)[:k]
    print("top k frequency", top_k_frequencies)
    top_k_periods = [int(data_size / x + 0.5) for x in top_k_frequencies]
    print("top k periods", top_k_periods)

    # remove duplicated periods if any
    periods = [x for i, x in enumerate(top_k_periods) if top_k_periods.index(x) == i]
    print('top periods after duplicated period removal', periods)

    if show:
        # plot input data
        plt.figure()
        plt.plot(df[target_column], label=target_column)
        plt.legend()
        plt.grid()

        # plot fft of input data
        plt.figure()
        plt.plot(np.abs(fft_result)[:half_data_size], label='fft')
        plt.legend()
        plt.grid()

        plt.show()

    return top_k_periods


def prepare_tabpfn_input(dataset_choice, item_id, target_column, periods, y_test_len, y_train_len):
    print("Preparing tabpfn input...")

    csv_file_path = f'./autogluon/{dataset_choice}_item_{item_id}.csv'
    df = pd.read_csv(csv_file_path)
    data = df[target_column]
    data_size = len(data)
    y_len = y_train_len + y_test_len
    # only data within visible length can be used for prediction of y_test
    visible_len = data_size - y_test_len
    y_start_index = data_size - y_len
    y_data = data[y_start_index:]

    output_data = [y_data]

    # different period may produce some duplicated x_start_index,
    # x_start_candidate_indices help take care of such cases
    x_start_candidate_indices = [y_start_index-p for p in periods]
    x_start_index = max(x_start_candidate_indices)
    x_start_index_i = x_start_candidate_indices.index(x_start_index)
    last_x_start_index = -1
    while x_start_index >= 0:
        x_last_index = x_start_index + y_len
        # x index is not duplicated one and it is within visible length
        if x_start_index != last_x_start_index and x_last_index <= visible_len:
            x_indices = [x for x in range(x_start_index, x_last_index)]
            x_data = data[x_indices]
            output_data.append(x_data)

        x_start_candidate_indices[x_start_index_i] -= periods[x_start_index_i]
        last_x_start_index = x_start_index
        x_start_index = max(x_start_candidate_indices)
        x_start_index_i = x_start_candidate_indices.index(x_start_index)

    output_data.reverse()

    n_column = len(output_data)
    headers = [str(x) for x in range(n_column)]
    output_df = pd.DataFrame(np.transpose(output_data).tolist(), columns=headers)
    output_df.to_csv(f'./autogluon/{dataset_choice}_item_{item_id}_s{y_len}_n{n_column}.csv', index=False)

    # n_column is the horizontal dimension of the data that input to tabpfn
    return n_column


def run_tabpfn(csv_file_path, target_column, train_ratio, show=True):
    print("Running tabpfn...")
    df = pd.read_csv(csv_file_path)
    cols = list(df.columns)
    cols.remove(target_column)

    X = df[cols]
    y = df[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_ratio, shuffle=False)

    print("train size", len(y_train))
    print("test size", len(y_test))

    # Initialize the regressor, fix the random state for result reproduction
    regressor = TabPFNRegressor(random_state=42)

    regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)

    # Evaluate the prediction
    mae = round(mean_absolute_error(y_test, predictions), 2)
    mse = round(mean_squared_error(y_test, predictions), 2)
    r2 = round(r2_score(y_test, predictions), 2)

    fig, ax = plt.subplots()
    ax.plot([x for x in range(len(y_test))], y_test, label="Ground Truth")
    ax.plot([x for x in range(len(y_test))], predictions, label="Predictions")
    ax.grid()
    ax.legend()
    fig.text(0.2, 0.02, f'mae:{mae}, mse:{mse}, r2:{r2}')
    if show:
        plt.show()
    else:
        plt.savefig(f'{csv_file_path}.pdf')
    plt.close()

    return [mae, mse, r2]


def main():

    # load the test datasets and save them in desired format,
    # check and run it at the very beginning
    # load_and_save_test_cases()

    # setups
    setups = [
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 0, 'y_test_len': 24, 'y_train_len': 12},    # 0
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 0, 'y_test_len': 24, 'y_train_len': 24},    # 1
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 0, 'y_test_len': 24, 'y_train_len': 36},    # 2
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 0, 'y_test_len': 24, 'y_train_len': 48},    # 3
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 0, 'y_test_len': 12, 'y_train_len': 12},    # 4
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 0, 'y_test_len': 12, 'y_train_len': 24},    # 5
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 0, 'y_test_len': 12, 'y_train_len': 36},    # 6
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 0, 'y_test_len': 12, 'y_train_len': 48},    # 7
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 1, 'y_test_len': 24, 'y_train_len': 12},    # 8
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 1, 'y_test_len': 24, 'y_train_len': 24},    # 9
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 1, 'y_test_len': 24, 'y_train_len': 36},    # 10
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 1, 'y_test_len': 24, 'y_train_len': 48},    # 11
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 1, 'y_test_len': 12, 'y_train_len': 12},    # 12
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 1, 'y_test_len': 12, 'y_train_len': 24},    # 13
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 1, 'y_test_len': 12, 'y_train_len': 36},    # 14
        {'dataset_choice': 'monash_tourism_monthly', 'item_id': 1, 'y_test_len': 12, 'y_train_len': 48},    # 15
        {'dataset_choice': 'm4_hourly', 'item_id': 0, 'y_test_len': 48, 'y_train_len': 24},                 # 16
        {'dataset_choice': 'm4_hourly', 'item_id': 0, 'y_test_len': 48, 'y_train_len': 48},                 # 17
        {'dataset_choice': 'm4_hourly', 'item_id': 0, 'y_test_len': 48, 'y_train_len': 72},                 # 18
        {'dataset_choice': 'm4_hourly', 'item_id': 0, 'y_test_len': 48, 'y_train_len': 96},                 # 19
        {'dataset_choice': 'm4_hourly', 'item_id': 0, 'y_test_len': 24, 'y_train_len': 24},                 # 20
        {'dataset_choice': 'm4_hourly', 'item_id': 0, 'y_test_len': 24, 'y_train_len': 48},                 # 21
        {'dataset_choice': 'm4_hourly', 'item_id': 0, 'y_test_len': 24, 'y_train_len': 72},                 # 22
        {'dataset_choice': 'm4_hourly', 'item_id': 0, 'y_test_len': 24, 'y_train_len': 96},                 # 23
        {'dataset_choice': 'm4_hourly', 'item_id': 1, 'y_test_len': 48, 'y_train_len': 24},                 # 24
        {'dataset_choice': 'm4_hourly', 'item_id': 1, 'y_test_len': 48, 'y_train_len': 48},                 # 25
        {'dataset_choice': 'm4_hourly', 'item_id': 1, 'y_test_len': 48, 'y_train_len': 72},                 # 26
        {'dataset_choice': 'm4_hourly', 'item_id': 1, 'y_test_len': 48, 'y_train_len': 96},                 # 27
        {'dataset_choice': 'm4_hourly', 'item_id': 1, 'y_test_len': 24, 'y_train_len': 24},                 # 28
        {'dataset_choice': 'm4_hourly', 'item_id': 1, 'y_test_len': 24, 'y_train_len': 48},                 # 29
        {'dataset_choice': 'm4_hourly', 'item_id': 1, 'y_test_len': 24, 'y_train_len': 72},                 # 30
        {'dataset_choice': 'm4_hourly', 'item_id': 1, 'y_test_len': 24, 'y_train_len': 96}                  # 31
    ]
    select_i = 25
    dataset_choice = setups[select_i]['dataset_choice']
    item_id = setups[select_i]['item_id']
    # m
    y_test_len = setups[select_i]['y_test_len']
    # l
    y_train_len = setups[select_i]['y_train_len']

    top_periods = calculate_top_k_periods(
        csv_file_path=f'./autogluon/{dataset_choice}_item_{item_id}.csv',
        target_column='target',
        pred_len=y_test_len,
        show=False
    )

    # use the top period, enough for the test dataset
    selected_periods = top_periods[:1]
    y_len = y_test_len + y_train_len

    n_column = prepare_tabpfn_input(
        dataset_choice=dataset_choice,
        item_id=item_id,
        target_column='target',
        periods=selected_periods,
        y_test_len=y_test_len,
        y_train_len=y_train_len
    )

    result = run_tabpfn(
        f'./autogluon/{dataset_choice}_item_{item_id}_s{y_len}_n{n_column}.csv',
        target_column=str(n_column - 1),
        train_ratio=y_train_len / (y_train_len + y_test_len)
    )

    print('---------------------------------------')
    print(f'dataset: {dataset_choice}, item id: {item_id}')
    print(f'y test length (m): {y_test_len}, y_train length (l): {y_train_len}')
    print(f'MAE: {result[0]}')


if __name__ == "__main__":
    main()
