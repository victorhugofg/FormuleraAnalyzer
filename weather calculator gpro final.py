#Pandas and Numpys
import pandas as pd
import numpy as np

#Ask for weather data
weather_data = input("Please enter the weather data: ")

#Split into list and convert value to float
weather_values = [float(value) for value in weather_data.split(',')]

#Create DF
df = pd.DataFrame({'WeatherData': weather_values})

#Calculate CumSum
df['CumulativeSum'] = df['WeatherData'].cumsum()

#Specify window size for moving average
window_size = 8

#Calculate MA
df['MovingAverage'] = df['WeatherData'].rolling(window=window_size).mean()

#Display DF
print(df)
