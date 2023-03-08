# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 03:26:47 2023

@author: SATHYA
"""

import neuralprophet as nph
from neuralprophet import NeuralProphet
# import plot_forecast
import pandas as pd
import numpy as np
from pandas.tseries.offsets import DateOffset
import matplotlib.pyplot as plt


# Load the data
#df = pd.read_excel("D:/SEM VIII/MINI PROJECT/AQI CODES/PROCESSED AQI DATA/ADILABAD_AQI.xlsx")
df=pd.read_excel("D:/SEM VIII/MINI PROJECT/AQI CODES/PROCESSED AQI DATA/ADILABAD_AQI - Copy.xlsx")
df= df.fillna(0)
df= df.replace(np.nan, 0)
df= df.replace("-", 0)
df.head(30)
columns = ["ds","month","y"]
df.columns = columns

df.index = pd.to_datetime(df['ds'])
df = df.drop_duplicates(subset=['ds'])

new_df = df.drop(["month"],axis=1)
#new_df=df.iloc[:,0]
final_df = df[["ds","y"]]
print(new_df.dtypes)

'''
model = nph.NeuralProphet(
    n_lags=12,     # number of lagged values to use as inputs
    n_forecasts=24, # number of time steps to forecast
    seasonality_mode='additive', # type of seasonality
    yearly_seasonality=True,     # include yearly seasonality
    weekly_seasonality=False,     # include weekly seasonality
    normalize='auto'
   
)


# fit the model to your data
#model.fit(new_df, freq='Y')
#model.fit(new_df)
#model.fit(new_df,freq='M',valid_p = 0.2)

last_date = final_df['ds'].max()
future = pd.DataFrame({
    'ds': pd.date_range(last_date, periods=84),
})


#future["year"] = df[["year"]].values
#future["aqi value"] = df[["aqi value"]].values

#future["aqi value"] = df[["aqi value"]].values

future["y"]=df[["y"]].values
print("future")
print(future.dtypes)

# make one-year forecast
future = model.make_future_dataframe(final_df, periods=84, n_historic_predictions=len(final_df))
forecast = model.predict(future)

# visualize the forecast
#fig = plot_forecast(forecast, figsize=(12, 8))
from matplotlib import pyplot
print(forecast[[]].head())
model.plot(forecast)
pyplot.show()
print("qwe")
'''


df.info()
new_df.info()

m =NeuralProphet()
df_train, df_val = m.split_df(new_df, freq='M', valid_p = 0.2)
metrics = m.fit(df_train, freq='M', validation_df=df_val)

future = m.make_future_dataframe(new_df, periods=24, n_historic_predictions=len(df))
forecast = m.predict(future)

fig_forecast = m.plot(forecast)
fig_components = m.plot_components(forecast)

fig_model = m.plot_parameters()

fig, ax = plt.subplots(figsize=(20, 8))
ax.plot(metrics["MAE"], '-o', label="Training Loss")  
ax.plot(metrics["MAE_val"], '-r', label="Validation Loss")
ax.legend(loc='center right', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=20)
ax.set_xlabel("Epoch", fontsize=28)
ax.set_ylabel("Loss", fontsize=28)
ax.set_title("Model Loss (MAE)", fontsize=28)

