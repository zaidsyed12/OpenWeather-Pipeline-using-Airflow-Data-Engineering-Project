import requests
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_openweather_etl():
    city_name = "Karachi"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    api_key = '************'
    full_url = base_url + city_name + "&appid=" + api_key
        
    def kelvin_to_celsius(temp_kelvin):
        return temp_kelvin - 273.15

    def weather_etl(full_url):
        r = requests.get(full_url)
        data = r.json()

        # Parsing data from JSON to Python dictionary
        transformed_data = {
            'City': data['name'],
            'Description': data['weather'][0]['description'],
            'Temperature (C)': kelvin_to_celsius(data['main']['temp']),
            'Feels Like (C)': kelvin_to_celsius(data['main']['feels_like']),
            'Minimum Temp (C)': kelvin_to_celsius(data['main']['temp_min']),
            'Maximum Temp (C)': kelvin_to_celsius(data['main']['temp_max']),
            'Pressure': data['main']['pressure'],
            'Humidity': data['main']['humidity'],
            'Wind Speed': data['wind']['speed'],
            'Time of Record': datetime.utcfromtimestamp(data['dt'] + data['timezone'])
        }

        df_transformed_data = pd.DataFrame([transformed_data])
        
        df_transformed_data.to_csv("s3://my-openweather-bucket/City_hourly_weather_data.csv", mode='a', index=False, header=False)

    weather_etl(full_url)

