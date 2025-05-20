---
annotations_creators:
- no-annotation
license: other
source_datasets:
- original
task_categories:
- time-series-forecasting
task_ids:
- univariate-time-series-forecasting
- multivariate-time-series-forecasting
pretty_name: Chronos datasets
dataset_info:
- config_name: dominick
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: im_0
    dtype: int64
  splits:
  - name: train
    num_bytes: 477140250
    num_examples: 100014
  download_size: 42290010
  dataset_size: 477140250
- config_name: electricity_15min
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: consumption_kW
    sequence: float64
  splits:
  - name: train
    num_bytes: 670989988
    num_examples: 370
  download_size: 284497403
  dataset_size: 670989988
  license: CC BY 4.0
  homepage: https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014
- config_name: ercot
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ns]
  - name: target
    sequence: float32
  splits:
  - name: train
    num_examples: 8
  download_size: 14504261
- config_name: exchange_rate
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float32
  splits:
  - name: train
    num_examples: 8
  download_size: 401501
  license: MIT
  homepage: https://github.com/laiguokun/multivariate-time-series-data/tree/master/exchange_rate
- config_name: m4_daily
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 160504176
    num_examples: 4227
  download_size: 65546675
  dataset_size: 160504176
  homepage: https://github.com/Mcompetitions/M4-methods
- config_name: m4_hourly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 5985544
    num_examples: 414
  download_size: 1336971
  dataset_size: 5985544
  homepage: https://github.com/Mcompetitions/M4-methods
- config_name: m4_monthly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 181372969
    num_examples: 48000
  download_size: 52772258
  dataset_size: 181372969
  homepage: https://github.com/Mcompetitions/M4-methods
- config_name: m4_quarterly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 39205397
    num_examples: 24000
  download_size: 13422579
  dataset_size: 39205397
  homepage: https://github.com/Mcompetitions/M4-methods
- config_name: m4_weekly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 5955806
    num_examples: 359
  download_size: 2556691
  dataset_size: 5955806
  homepage: https://github.com/Mcompetitions/M4-methods
- config_name: m4_yearly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 14410042
    num_examples: 23000
  download_size: 5488601
  dataset_size: 14410042
  homepage: https://github.com/Mcompetitions/M4-methods
- config_name: m5
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: item_id
    dtype: string
  - name: target
    sequence: float32
  - name: dept_id
    dtype: string
  - name: cat_id
    dtype: string
  - name: store_id
    dtype: string
  - name: state_id
    dtype: string
  splits:
  - name: train
    num_bytes: 574062630
    num_examples: 30490
  download_size: 78063286
  dataset_size: 574062630
  homepage: https://www.kaggle.com/competitions/m5-forecasting-accuracy/rules
- config_name: mexico_city_bikes
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 618999406
    num_examples: 494
  download_size: 103206946
  dataset_size: 618999406
  homepage: https://ecobici.cdmx.gob.mx/en/open-data/
- config_name: monash_australian_electricity
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 18484319
    num_examples: 5
  download_size: 16856156
  dataset_size: 18484319
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_car_parts
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 2232790
    num_examples: 2674
  download_size: 70278
  dataset_size: 2232790
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_cif_2016
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 115096
    num_examples: 72
  download_size: 70876
  dataset_size: 115096
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_covid_deaths
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 907326
    num_examples: 266
  download_size: 58957
  dataset_size: 907326
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_electricity_hourly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 135103443
    num_examples: 321
  download_size: 31139117
  dataset_size: 135103443
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_electricity_weekly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 807315
    num_examples: 321
  download_size: 333563
  dataset_size: 807315
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_fred_md
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 1248369
    num_examples: 107
  download_size: 412207
  dataset_size: 1248369
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_hospital
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: int64
  splits:
  - name: train
    num_examples: 767
  download_size: 117038
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_kdd_cup_2018
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: city
    dtype: string
  - name: station
    dtype: string
  - name: measurement
    dtype: string
  splits:
  - name: train
    num_bytes: 47091540
    num_examples: 270
  download_size: 8780105
  dataset_size: 47091540
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_london_smart_meters
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 2664567976
    num_examples: 5560
  download_size: 597389119
  dataset_size: 2664567976
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_m1_monthly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 907691
    num_examples: 617
  download_size: 244372
  dataset_size: 907691
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_m1_quarterly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 162961
    num_examples: 203
  download_size: 48439
  dataset_size: 162961
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_m1_yearly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 75679
    num_examples: 181
  download_size: 30754
  dataset_size: 75679
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_m3_monthly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 2708124
    num_examples: 1428
  download_size: 589699
  dataset_size: 2708124
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_m3_quarterly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 606428
    num_examples: 756
  download_size: 188543
  dataset_size: 606428
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_m3_yearly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 305359
    num_examples: 645
  download_size: 100184
  dataset_size: 305359
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_nn5_weekly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float32
  splits:
  - name: train
    num_examples: 111
  download_size: 64620
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_pedestrian_counts
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: int64
  splits:
  - name: train
    num_bytes: 50118790
    num_examples: 66
  download_size: 12377357
  dataset_size: 50118790
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_rideshare
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: source_location
    dtype: string
  - name: provider_name
    dtype: string
  - name: provider_service
    dtype: string
  - name: price_min
    sequence: float64
  - name: price_mean
    sequence: float64
  - name: price_max
    sequence: float64
  - name: distance_min
    sequence: float64
  - name: distance_mean
    sequence: float64
  - name: distance_max
    sequence: float64
  - name: surge_min
    sequence: float64
  - name: surge_mean
    sequence: float64
  - name: surge_max
    sequence: float64
  - name: api_calls
    sequence: float64
  - name: temp
    sequence: float64
  - name: rain
    sequence: float64
  - name: humidity
    sequence: float64
  - name: clouds
    sequence: float64
  - name: wind
    sequence: float64
  splits:
  - name: train
    num_bytes: 10819910
    num_examples: 156
  download_size: 781873
  dataset_size: 10819910
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_saugeenday
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: T1
    sequence: float64
  splits:
  - name: train
    num_bytes: 379875
    num_examples: 1
  download_size: 222678
  dataset_size: 379875
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_temperature_rain
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: t_mean
    sequence: float64
  - name: prcp_sum
    sequence: float64
  - name: t_max
    sequence: float64
  - name: t_min
    sequence: float64
  - name: fcst_0_dailypop
    sequence: float64
  - name: fcst_0_dailypop1
    sequence: float64
  - name: fcst_0_dailypop10
    sequence: float64
  - name: fcst_0_dailypop15
    sequence: float64
  - name: fcst_0_dailypop25
    sequence: float64
  - name: fcst_0_dailypop5
    sequence: float64
  - name: fcst_0_dailypop50
    sequence: float64
  - name: fcst_0_dailyprecip
    sequence: float64
  - name: fcst_0_dailyprecip10pct
    sequence: float64
  - name: fcst_0_dailyprecip25pct
    sequence: float64
  - name: fcst_0_dailyprecip50pct
    sequence: float64
  - name: fcst_0_dailyprecip75pct
    sequence: float64
  - name: fcst_1_dailypop
    sequence: float64
  - name: fcst_1_dailypop1
    sequence: float64
  - name: fcst_1_dailypop10
    sequence: float64
  - name: fcst_1_dailypop15
    sequence: float64
  - name: fcst_1_dailypop25
    sequence: float64
  - name: fcst_1_dailypop5
    sequence: float64
  - name: fcst_1_dailypop50
    sequence: float64
  - name: fcst_1_dailyprecip
    sequence: float64
  - name: fcst_1_dailyprecip10pct
    sequence: float64
  - name: fcst_1_dailyprecip25pct
    sequence: float64
  - name: fcst_1_dailyprecip50pct
    sequence: float64
  - name: fcst_1_dailyprecip75pct
    sequence: float64
  - name: fcst_2_dailypop
    sequence: float64
  - name: fcst_2_dailypop1
    sequence: float64
  - name: fcst_2_dailypop10
    sequence: float64
  - name: fcst_2_dailypop15
    sequence: float64
  - name: fcst_2_dailypop25
    sequence: float64
  - name: fcst_2_dailypop5
    sequence: float64
  - name: fcst_2_dailypop50
    sequence: float64
  - name: fcst_2_dailyprecip
    sequence: float64
  - name: fcst_2_dailyprecip10pct
    sequence: float64
  - name: fcst_2_dailyprecip25pct
    sequence: float64
  - name: fcst_2_dailyprecip50pct
    sequence: float64
  - name: fcst_2_dailyprecip75pct
    sequence: float64
  - name: fcst_3_dailypop
    sequence: float64
  - name: fcst_3_dailypop1
    sequence: float64
  - name: fcst_3_dailypop10
    sequence: float64
  - name: fcst_3_dailypop15
    sequence: float64
  - name: fcst_3_dailypop25
    sequence: float64
  - name: fcst_3_dailypop5
    sequence: float64
  - name: fcst_3_dailypop50
    sequence: float64
  - name: fcst_3_dailyprecip
    sequence: float64
  - name: fcst_3_dailyprecip10pct
    sequence: float64
  - name: fcst_3_dailyprecip25pct
    sequence: float64
  - name: fcst_3_dailyprecip50pct
    sequence: float64
  - name: fcst_3_dailyprecip75pct
    sequence: float64
  - name: fcst_4_dailypop
    sequence: float64
  - name: fcst_4_dailypop1
    sequence: float64
  - name: fcst_4_dailypop10
    sequence: float64
  - name: fcst_4_dailypop15
    sequence: float64
  - name: fcst_4_dailypop25
    sequence: float64
  - name: fcst_4_dailypop5
    sequence: float64
  - name: fcst_4_dailypop50
    sequence: float64
  - name: fcst_4_dailyprecip
    sequence: float64
  - name: fcst_4_dailyprecip10pct
    sequence: float64
  - name: fcst_4_dailyprecip25pct
    sequence: float64
  - name: fcst_4_dailyprecip50pct
    sequence: float64
  - name: fcst_4_dailyprecip75pct
    sequence: float64
  - name: fcst_5_dailypop
    sequence: float64
  - name: fcst_5_dailypop1
    sequence: float64
  - name: fcst_5_dailypop10
    sequence: float64
  - name: fcst_5_dailypop15
    sequence: float64
  - name: fcst_5_dailypop25
    sequence: float64
  - name: fcst_5_dailypop5
    sequence: float64
  - name: fcst_5_dailypop50
    sequence: float64
  - name: fcst_5_dailyprecip
    sequence: float64
  - name: fcst_5_dailyprecip10pct
    sequence: float64
  - name: fcst_5_dailyprecip25pct
    sequence: float64
  - name: fcst_5_dailyprecip50pct
    sequence: float64
  - name: fcst_5_dailyprecip75pct
    sequence: float64
  splits:
  - name: train
    num_bytes: 188598927
    num_examples: 422
  download_size: 44967856
  dataset_size: 188598927
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_tourism_monthly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 1755434
    num_examples: 366
  download_size: 334951
  dataset_size: 1755434
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_tourism_quarterly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 688817
    num_examples: 427
  download_size: 177407
  dataset_size: 688817
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_tourism_yearly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 213954
    num_examples: 518
  download_size: 81479
  dataset_size: 213954
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_traffic
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 241983226
    num_examples: 862
  download_size: 52748547
  dataset_size: 241983226
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: monash_weather
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: subset
    dtype: string
  splits:
  - name: train
    num_bytes: 688598539
    num_examples: 3010
  download_size: 133164027
  dataset_size: 688598539
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: nn5
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float32
  splits:
  - name: train
    num_examples: 111
  download_size: 203096
  homepage: http://www.neural-forecasting-competition.com/downloads/NN5/datasets/download.htm
- config_name: solar
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: power_mw
    sequence: float64
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: capacity_mw
    dtype: float64
  - name: subset
    dtype: string
  splits:
  - name: train
    num_bytes: 8689093932
    num_examples: 5166
  download_size: 1507924920
  dataset_size: 8689093932
  homepage: https://www.nrel.gov/grid/solar-power-data.html
- config_name: solar_1h
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: power_mw
    sequence: float64
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: capacity_mw
    dtype: float64
  - name: subset
    dtype: string
  splits:
  - name: train
    num_bytes: 724361772
    num_examples: 5166
  download_size: 124515417
  dataset_size: 724361772
  homepage: https://www.nrel.gov/grid/solar-power-data.html
- config_name: taxi_1h
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: subset
    dtype: string
  - name: lat
    dtype: float64
  - name: lng
    dtype: float64
  splits:
  - name: train
    num_bytes: 28832500
    num_examples: 2428
  download_size: 2265297
  dataset_size: 28832500
  license: Apache 2.0
  homepage: https://github.com/mbohlkeschneider/gluon-ts/tree/mv_release/datasets
- config_name: taxi_30min
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: subset
    dtype: string
  - name: lat
    dtype: float64
  - name: lng
    dtype: float64
  splits:
  - name: train
    num_bytes: 57560596
    num_examples: 2428
  download_size: 4541244
  dataset_size: 57560596
  license: Apache 2.0
  homepage: https://github.com/mbohlkeschneider/gluon-ts/tree/mv_release/datasets
- config_name: training_corpus_kernel_synth_1m
  features:
  - name: target
    sequence: float64
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  splits:
  - name: train
    num_examples: 1000000
  download_size: 8313239368
- config_name: training_corpus_tsmixup_10m
  features:
  - name: target
    sequence: float64
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  splits:
  - name: train
    num_examples: 10000000
  download_size: 82189589906
- config_name: uber_tlc_daily
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: int64
  splits:
  - name: train
    num_examples: 262
  download_size: 84747
  homepage: https://github.com/fivethirtyeight/uber-tlc-foil-response
- config_name: uber_tlc_hourly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: int64
  splits:
  - name: train
    num_examples: 262
  download_size: 1878515
  homepage: https://github.com/fivethirtyeight/uber-tlc-foil-response
- config_name: ushcn_daily
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: state
    dtype: string
  - name: coop_id
    dtype: int64
  - name: PRCP
    sequence: float64
  - name: SNOW
    sequence: float64
  - name: SNWD
    sequence: float64
  - name: TMAX
    sequence: float64
  - name: TMIN
    sequence: float64
  splits:
  - name: train
    num_bytes: 2259905202
    num_examples: 1218
  download_size: 221089890
  dataset_size: 2259905202
  homepage: https://data.ess-dive.lbl.gov/portals/CDIAC
- config_name: weatherbench_daily
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float32
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: level
    dtype: float64
  - name: subset
    dtype: string
  splits:
  - name: train
    num_bytes: 39510157312
    num_examples: 225280
  download_size: 18924392742
  dataset_size: 39510157312
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_10m_u_component_of_wind
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: float64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 2048
  download_size: 7292845757
  dataset_size: 8617472000
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_10m_v_component_of_wind
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: float64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 2048
  download_size: 7292352508
  dataset_size: 8617472000
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_2m_temperature
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: float64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 2048
  download_size: 7276396852
  dataset_size: 8617453568
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_geopotential
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: int64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 26624
  download_size: 87305564613
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_potential_vorticity
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: int64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 26624
  download_size: 92426240043
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_relative_humidity
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: int64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 26624
  download_size: 94728788382
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_specific_humidity
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: int64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 26624
  download_size: 85139896451
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_temperature
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: int64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 26624
  download_size: 94081539079
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_toa_incident_solar_radiation
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: float64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 2048
  download_size: 6057953007
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_total_cloud_cover
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: float64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 2048
  download_size: 6628258398
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_total_precipitation
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: float64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 2048
  download_size: 6473160755
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_u_component_of_wind
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: int64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 26624
  download_size: 94801498563
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_v_component_of_wind
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: int64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 26624
  download_size: 94800557482
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_hourly_vorticity
  features:
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: target
    sequence: float32
  - name: level
    dtype: int64
  - name: timestamp
    sequence: timestamp[ms]
  - name: subset
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_examples: 26624
  download_size: 94720960560
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: weatherbench_weekly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float32
  - name: latitude
    dtype: float64
  - name: longitude
    dtype: float64
  - name: level
    dtype: float64
  - name: subset
    dtype: string
  splits:
  - name: train
    num_bytes: 5656029184
    num_examples: 225280
  download_size: 2243012083
  dataset_size: 5656029184
  license: MIT
  homepage: https://github.com/pangeo-data/WeatherBench
- config_name: wiki_daily_100k
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  - name: page_name
    dtype: string
  splits:
  - name: train
    num_bytes: 4389782678
    num_examples: 100000
  download_size: 592554033
  dataset_size: 4389782678
  license: CC0
  homepage: https://dumps.wikimedia.org/other/pageviews/readme.html
- config_name: wind_farms_daily
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 1919187
    num_examples: 337
  download_size: 598834
  dataset_size: 1919187
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
- config_name: wind_farms_hourly
  features:
  - name: id
    dtype: string
  - name: timestamp
    sequence: timestamp[ms]
  - name: target
    sequence: float64
  splits:
  - name: train
    num_bytes: 45917027
    num_examples: 337
  download_size: 12333116
  dataset_size: 45917027
  license: CC BY 4.0
  homepage: https://zenodo.org/communities/forecasting
configs:
- config_name: dominick
  data_files:
  - split: train
    path: dominick/train-*
- config_name: electricity_15min
  data_files:
  - split: train
    path: electricity_15min/train-*
- config_name: ercot
  data_files:
  - split: train
    path: ercot/train-*
- config_name: exchange_rate
  data_files:
  - split: train
    path: exchange_rate/train-*
- config_name: m4_daily
  data_files:
  - split: train
    path: m4_daily/train-*
- config_name: m4_hourly
  data_files:
  - split: train
    path: m4_hourly/train-*
- config_name: m4_monthly
  data_files:
  - split: train
    path: m4_monthly/train-*
- config_name: m4_quarterly
  data_files:
  - split: train
    path: m4_quarterly/train-*
- config_name: m4_weekly
  data_files:
  - split: train
    path: m4_weekly/train-*
- config_name: m4_yearly
  data_files:
  - split: train
    path: m4_yearly/train-*
- config_name: m5
  data_files:
  - split: train
    path: m5/train-*
- config_name: mexico_city_bikes
  data_files:
  - split: train
    path: mexico_city_bikes/train-*
- config_name: monash_australian_electricity
  data_files:
  - split: train
    path: monash_australian_electricity/train-*
- config_name: monash_car_parts
  data_files:
  - split: train
    path: monash_car_parts/train-*
- config_name: monash_cif_2016
  data_files:
  - split: train
    path: monash_cif_2016/train-*
- config_name: monash_covid_deaths
  data_files:
  - split: train
    path: monash_covid_deaths/train-*
- config_name: monash_electricity_hourly
  data_files:
  - split: train
    path: monash_electricity_hourly/train-*
- config_name: monash_electricity_weekly
  data_files:
  - split: train
    path: monash_electricity_weekly/train-*
- config_name: monash_fred_md
  data_files:
  - split: train
    path: monash_fred_md/train-*
- config_name: monash_hospital
  data_files:
  - split: train
    path: monash_hospital/train-*
- config_name: monash_kdd_cup_2018
  data_files:
  - split: train
    path: monash_kdd_cup_2018/train-*
- config_name: monash_london_smart_meters
  data_files:
  - split: train
    path: monash_london_smart_meters/train-*
- config_name: monash_m1_monthly
  data_files:
  - split: train
    path: monash_m1_monthly/train-*
- config_name: monash_m1_quarterly
  data_files:
  - split: train
    path: monash_m1_quarterly/train-*
- config_name: monash_m1_yearly
  data_files:
  - split: train
    path: monash_m1_yearly/train-*
- config_name: monash_m3_monthly
  data_files:
  - split: train
    path: monash_m3_monthly/train-*
- config_name: monash_m3_quarterly
  data_files:
  - split: train
    path: monash_m3_quarterly/train-*
- config_name: monash_m3_yearly
  data_files:
  - split: train
    path: monash_m3_yearly/train-*
- config_name: monash_nn5_weekly
  data_files:
  - split: train
    path: monash_nn5_weekly/train-*
- config_name: monash_pedestrian_counts
  data_files:
  - split: train
    path: monash_pedestrian_counts/train-*
- config_name: monash_rideshare
  data_files:
  - split: train
    path: monash_rideshare/train-*
- config_name: monash_saugeenday
  data_files:
  - split: train
    path: monash_saugeenday/train-*
- config_name: monash_temperature_rain
  data_files:
  - split: train
    path: monash_temperature_rain/train-*
- config_name: monash_tourism_monthly
  data_files:
  - split: train
    path: monash_tourism_monthly/train-*
- config_name: monash_tourism_quarterly
  data_files:
  - split: train
    path: monash_tourism_quarterly/train-*
- config_name: monash_tourism_yearly
  data_files:
  - split: train
    path: monash_tourism_yearly/train-*
- config_name: monash_traffic
  data_files:
  - split: train
    path: monash_traffic/train-*
- config_name: monash_weather
  data_files:
  - split: train
    path: monash_weather/train-*
- config_name: nn5
  data_files:
  - split: train
    path: nn5/train-*
- config_name: solar
  data_files:
  - split: train
    path: solar/train-*
- config_name: solar_1h
  data_files:
  - split: train
    path: solar_1h/train-*
- config_name: taxi_1h
  data_files:
  - split: train
    path: taxi_1h/train-*
- config_name: taxi_30min
  data_files:
  - split: train
    path: taxi_30min/train-*
- config_name: training_corpus_kernel_synth_1m
  data_files:
  - split: train
    path: training_corpus/kernel_synth_1m/train-*
- config_name: training_corpus_tsmixup_10m
  data_files:
  - split: train
    path: training_corpus/tsmixup_10m/train-*
- config_name: uber_tlc_daily
  data_files:
  - split: train
    path: uber_tlc_daily/train-*
- config_name: uber_tlc_hourly
  data_files:
  - split: train
    path: uber_tlc_hourly/train-*
- config_name: ushcn_daily
  data_files:
  - split: train
    path: ushcn_daily/train-*
- config_name: weatherbench_daily
  data_files:
  - split: train
    path: weatherbench_daily/train-*
- config_name: weatherbench_hourly_10m_u_component_of_wind
  data_files:
  - split: train
    path: weatherbench_hourly/10m_u_component_of_wind/train-*
- config_name: weatherbench_hourly_10m_v_component_of_wind
  data_files:
  - split: train
    path: weatherbench_hourly/10m_v_component_of_wind/train-*
- config_name: weatherbench_hourly_2m_temperature
  data_files:
  - split: train
    path: weatherbench_hourly/2m_temperature/train-*
- config_name: weatherbench_hourly_geopotential
  data_files:
  - split: train
    path: weatherbench_hourly/geopotential/train-*
- config_name: weatherbench_hourly_potential_vorticity
  data_files:
  - split: train
    path: weatherbench_hourly/potential_vorticity/train-*
- config_name: weatherbench_hourly_relative_humidity
  data_files:
  - split: train
    path: weatherbench_hourly/relative_humidity/train-*
- config_name: weatherbench_hourly_specific_humidity
  data_files:
  - split: train
    path: weatherbench_hourly/specific_humidity/train-*
- config_name: weatherbench_hourly_temperature
  data_files:
  - split: train
    path: weatherbench_hourly/temperature/train-*
- config_name: weatherbench_hourly_toa_incident_solar_radiation
  data_files:
  - split: train
    path: weatherbench_hourly/toa_incident_solar_radiation/train-*
- config_name: weatherbench_hourly_total_cloud_cover
  data_files:
  - split: train
    path: weatherbench_hourly/total_cloud_cover/train-*
- config_name: weatherbench_hourly_total_precipitation
  data_files:
  - split: train
    path: weatherbench_hourly/total_precipitation/train-*
- config_name: weatherbench_hourly_u_component_of_wind
  data_files:
  - split: train
    path: weatherbench_hourly/u_component_of_wind/train-*
- config_name: weatherbench_hourly_v_component_of_wind
  data_files:
  - split: train
    path: weatherbench_hourly/v_component_of_wind/train-*
- config_name: weatherbench_hourly_vorticity
  data_files:
  - split: train
    path: weatherbench_hourly/vorticity/train-*
- config_name: weatherbench_weekly
  data_files:
  - split: train
    path: weatherbench_weekly/train-*
- config_name: wiki_daily_100k
  data_files:
  - split: train
    path: wiki_daily_100k/train-*
- config_name: wind_farms_daily
  data_files:
  - split: train
    path: wind_farms_daily/train-*
- config_name: wind_farms_hourly
  data_files:
  - split: train
    path: wind_farms_hourly/train-*
---

# Chronos datasets

Time series datasets used for training and evaluation of the [Chronos](https://github.com/amazon-science/chronos-forecasting) forecasting models.

Note that some Chronos datasets (`ETTh`, `ETTm`, `brazilian_cities_temperature` and `spanish_energy_and_weather`) that rely on a custom builder script are available in the companion repo [`autogluon/chronos_datasets_extra`](https://huggingface.co/datasets/autogluon/chronos_datasets_extra).

See the [paper](https://arxiv.org/abs/2403.07815) for more information.

## Data format and usage

The recommended way to use these datasets is via https://github.com/autogluon/fev.

All datasets satisfy the following high-level schema:
- Each dataset row corresponds to a single (univariate or multivariate) time series.
- There exists one column with name `id` and type `string` that contains the unique identifier of each time series.
- There exists one column of type `Sequence` with dtype `timestamp[ms]`. This column contains the timestamps of the observations. Timestamps are guaranteed to have a regular frequency that can be obtained with [`pandas.infer_freq`](https://pandas.pydata.org/docs/reference/api/pandas.infer_freq.html).
- There exists at least one column of type `Sequence` with numeric (`float`, `double`, or `int`) dtype. These columns can be interpreted as target time series.
- For each row, all columns of type `Sequence` have same length.
- Remaining columns of types other than `Sequence` (e.g., `string` or `float`) can be interpreted as static covariates.

Datasets can be loaded using the 🤗 [`datasets`](https://huggingface.co/docs/datasets/en/index) library
```python
import datasets

ds = datasets.load_dataset("autogluon/chronos_datasets", "m4_daily", split="train")
ds.set_format("numpy")  # sequences returned as numpy arrays
```

> **NOTE:**  The `train` split of all datasets contains the full time series and has no relation to the train/test split used in the Chronos paper.


Example entry in the `m4_daily` dataset
```python
>>> ds[0]
{'id': 'T000000',
 'timestamp': array(['1994-03-01T12:00:00.000', '1994-03-02T12:00:00.000',
        '1994-03-03T12:00:00.000', ..., '1996-12-12T12:00:00.000',
        '1996-12-13T12:00:00.000', '1996-12-14T12:00:00.000'],
       dtype='datetime64[ms]'),
 'target': array([1017.1, 1019.3, 1017. , ..., 2071.4, 2083.8, 2080.6], dtype=float32),
 'category': 'Macro'}
```

## Changelog
- **v1.3.0 (2025-03-05)**: Fix incorrect timestamp frequency for `monash_hospital`
- **v1.2.0 (2025-01-03)**: Fix incorrect timestamp frequency for `dominick`
- **v1.1.0 (2024-11-14)**: Fix irregular timestamp frequency for `m4_quarterly`
- **v1.0.0 (2024-07-24)**: Initial release

### Converting to pandas
We can easily convert data in such format to a long format data frame
```python
def to_pandas(ds: datasets.Dataset) -> "pd.DataFrame":
    """Convert dataset to long data frame format."""
    sequence_columns = [col for col in ds.features if isinstance(ds.features[col], datasets.Sequence)]
    return ds.to_pandas().explode(sequence_columns).infer_objects()
```
Example output
```python
>>> print(to_pandas(ds).head())
        id           timestamp  target category
0  T000000 1994-03-01 12:00:00  1017.1    Macro
1  T000000 1994-03-02 12:00:00  1019.3    Macro
2  T000000 1994-03-03 12:00:00  1017.0    Macro
3  T000000 1994-03-04 12:00:00  1019.2    Macro
4  T000000 1994-03-05 12:00:00  1018.7    Macro
```


### Dealing with large datasets
Note that some datasets, such as subsets of WeatherBench, are extremely large (~100GB). To work with them efficiently, we recommend either loading them from disk (files will be downloaded to disk, but won't be all loaded into memory)
```python
ds = datasets.load_dataset("autogluon/chronos_datasets", "weatherbench_daily", keep_in_memory=False, split="train")
```
or, for the largest datasets like `weatherbench_hourly_temperature`, reading them in streaming format (chunks will be downloaded one at a time)
```python
ds = datasets.load_dataset("autogluon/chronos_datasets", "weatherbench_hourly_temperature", streaming=True, split="train")
```

## Chronos training corpus with TSMixup & KernelSynth
The training corpus used for training the Chronos models can be loaded via the configs `training_corpus_tsmixup_10m` (10M TSMixup augmentations of real-world data) and `training_corpus_kernel_synth_1m` (1M synthetic time series generated with KernelSynth), e.g.,
```python
ds = datasets.load_dataset("autogluon/chronos_datasets", "training_corpus_tsmixup_10m", streaming=True, split="train")
```
Note that since data in the training corpus was obtained by combining various synthetic & real-world time series, the timestamps contain dummy values that have no connection to the original data.

## License
Different datasets available in this collection are distributed under different open source licenses. Please see `ds.info.license` and `ds.info.homepage` for each individual dataset.

## Citation

If you find these datasets useful for your research, please consider citing the associated paper:
```markdown
@article{ansari2024chronos,
  author  = {Ansari, Abdul Fatir and Stella, Lorenzo and Turkmen, Caner and Zhang, Xiyuan and Mercado, Pedro and Shen, Huibin and Shchur, Oleksandr and Rangapuram, Syama Syndar and Pineda Arango, Sebastian and Kapoor, Shubham and Zschiegner, Jasper and Maddix, Danielle C. and Wang, Hao and Mahoney, Michael W. and Torkkola, Kari and Gordon Wilson, Andrew and Bohlke-Schneider, Michael and Wang, Yuyang},
  title   = {Chronos: Learning the Language of Time Series},
  journal = {arXiv preprint arXiv:2403.07815},
  year    = {2024}
}
```
