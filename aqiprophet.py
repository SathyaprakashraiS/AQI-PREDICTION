# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 03:26:47 2023

@author: SATHYA
"""

import neuralprophet as nph
# import plot_forecast
import pandas as pd
import numpy as np
from pandas.tseries.offsets import DateOffset
import matplotlib.pyplot as plt


# Load the data
df = pd.read_excel("D:/SEM VIII/MINI PROJECT/AQI CODES/PROCESSED AQI DATA/ADILABAD_AQI.xlsx")
df.head(30)
columns = ["year","month","aqi value"]
df.columns = columns
#df.index = pd.to_datetime(df['ds'])
#df = df.drop_duplicates(subset=['ds'])

new_df = df.drop(["year"],axis=1)
final_df = df[["year","aqi value"]]
print(new_df.dtypes)


model = nph.NeuralProphet(
    n_lags=15,     # number of lagged values to use as inputs
    n_forecasts=7, # number of time steps to forecast
    seasonality_mode='additive', # type of seasonality
    yearly_seasonality=True,     # include yearly seasonality
    weekly_seasonality=True,     # include weekly seasonality
    normalize='auto'
   
)

# fit the model to your data
model.fit(new_df, freq='D')
last_date = final_df['ds'].max()
future = pd.DataFrame({
    'ds': pd.date_range(last_date, periods=365),
})


future["month"] = df[["month"]].values
future["aqi value"] = df[["aqi value"]].values
future["y"] = df[["y"]].values
print("future")
print(future.dtypes)

# make one-year forecast
# future = model.make_future_dataframe(final_df, periods=365, n_historic_predictions=len(final_df))
# forecast = model.predict(future)

# visualize the forecast


# fig = plot_forecast(forecast, figsize=(12, 8))


print("qwe")