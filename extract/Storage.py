import os
import pandas as pd

def save_weather_data(dataframe, file_name):
    if os.path.exists(file_name):
        print(f"{file_name} is already exist! Appending new observations into {file_name}...")
        dataframe.to_csv(file_name, mode='a', header=False, index=False,encoding='utf-8')
        print('Done...!')
    else:
        print(f"Creating dataframe...")
        dataframe.to_csv('raw_weather_data.csv', index=False, encoding='utf-8')
        print('Done...!')
