from pprint import pprint
from dotenv import *
import requests
import os
load_dotenv()

def CurrentWeather():
    print("GET CURRENT WEATHER REPORT")
    city=input("please enter a city name:")
    req_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weatherData=requests.get(req_url).json()

    #To easily read and see data in a json file
    #pprint(weatherData)
    print(f"The weather conditions are \nName:{weatherData["name"]}\nWind:{weatherData["wind"]}\nCurrent Temp{weatherData["main"]["temp"]}")

CurrentWeather()
