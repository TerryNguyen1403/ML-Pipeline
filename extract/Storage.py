import os
import pandas as pd

def save_weather_data(dataframe, file_name):
    """
    Save weather data to CSV file
    
    Parameters:
    - dataframe: DataFrame to save
    - file_name: Path to save the file
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        
        if os.path.exists(file_name):
            print(f"{file_name} is already exist! Appending new observations into {file_name}...")
            dataframe.to_csv(file_name, mode='a', header=False, index=False, encoding='utf-8')
            print('Done...!')
        else:
            print(f"Creating dataframe at {file_name}...")
            dataframe.to_csv(file_name, index=False, encoding='utf-8')
            print('Done...!')
            
    except Exception as e:
        print(f"Error saving data: {e}")
        return False
    
    return True
