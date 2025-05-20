# This script is mainly from the demo script of TapPFN-TS in Google Colab
# https://colab.research.google.com/github/liam-sbhoo/tabpfn-time-series/blob/main/demo.ipynb
# This script is for the purpose of result comparison with our method

# setup
dataset_metadata = {
    "monash_tourism_monthly": {"prediction_length": 24},
    "m4_hourly": {"prediction_length": 48},
}

dataset_choice = "m4_hourly"
num_time_series_subset = 2

from datasets import load_dataset
from autogluon.timeseries import TimeSeriesDataFrame

from tabpfn_time_series.data_preparation import to_gluonts_univariate, generate_test_X

prediction_length = dataset_metadata[dataset_choice]['prediction_length']
# dataset = load_dataset("autogluon/chronos_datasets", dataset_choice)
# load from local disk
dataset = load_dataset(f"autogluon/chronos_datasets/{dataset_choice}")
tsdf = TimeSeriesDataFrame(to_gluonts_univariate(dataset['train']))
tsdf = tsdf[tsdf.index.get_level_values('item_id').isin(tsdf.item_ids[:num_time_series_subset])]
train_tsdf, test_tsdf_ground_truth = tsdf.train_test_split(prediction_length=prediction_length)
test_tsdf = generate_test_X(train_tsdf, prediction_length)

# from tabpfn_time_series.plot import plot_actual_ts
#
# plot_actual_ts(train_tsdf, test_tsdf_ground_truth)

from tabpfn_time_series import FeatureTransformer, DefaultFeatures

selected_features = [
    DefaultFeatures.add_running_index,
    DefaultFeatures.add_calendar_features,
]

train_tsdf, test_tsdf = FeatureTransformer.add_features(
    train_tsdf, test_tsdf, selected_features
)

# train_tsdf.head()
# test_tsdf.head()

from tabpfn_time_series import TabPFNTimeSeriesPredictor, TabPFNMode

# you may want to set your own tabpfn token
from tabpfn_client import set_access_token
# set_access_token(your_tabpfn_token)
set_access_token(
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiMTdkNjgyNjItZDdjYS00OThlLTgyNDEtMjZiZjhlOTdmOGZkIiwiZXhwIjoxNzc2OTI0NTA4fQ.lbmLZWFlLQ8jZgDqt69gwLGW3gKhev0NmsM3mOGcBzQ'
)

# tabpfn setup, copy from the default setup TABPFN_TS_DEFAULT_CONFIG
# fix the random state for result reproduction
# set the output type to "mean" for comparison purpose
my_config =  {
    "tabpfn_internal": {
        "model_path": "2noar4o2",
        "random_state": 42
    },
    "tabpfn_output_selection": "mean",  # mean or median
}

predictor = TabPFNTimeSeriesPredictor(
    tabpfn_mode=TabPFNMode.CLIENT,
    config=my_config
)

pred = predictor.predict(train_tsdf, test_tsdf)

# evaluate the prediction results
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

for item_id, gt_value in test_tsdf_ground_truth['target'].groupby('item_id'):
    gt_value = gt_value[-prediction_length:]
    pred_value = pred['target'].groupby('item_id').get_group(item_id)

    # import pandas as pd
    # pd.set_option('display.max_rows', None)
    # print("Ground Truth:\n", gt_value)
    # print("Prediction:\n", pred_value)

    mae = round(mean_absolute_error(gt_value, pred_value), 2)
    mse = round(mean_squared_error(gt_value, pred_value), 2)
    r2 = round(r2_score(gt_value, pred_value), 2)

    print('---------------------------------------')
    print(f'datsset: {dataset_choice}, item id: {item_id}, prediction length: {prediction_length}')
    print(f'MAE: {mae}')
    # print(f'MAE: {mae}, MSE: {mse}, R²: {r2}')


# plot the prediction
from tabpfn_time_series.plot import plot_pred_and_actual_ts

plot_pred_and_actual_ts(
    train=train_tsdf,
    test=test_tsdf_ground_truth,
    pred=pred,
)
