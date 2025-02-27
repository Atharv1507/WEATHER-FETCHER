from pprint import pprint
from dotenv import *
import requests
import os

load_dotenv()

end=""
print("GET CURRENT WEATHER REPORT")

def CurrentWeather():
 try:
    city=input("please enter a city name:")   
    req_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weatherData=requests.get(req_url).json()
    print(f"\nThe weather conditions are \nName:{weatherData["name"]}\nWind:{weatherData["wind"]}\nCurrent Temp:{weatherData["main"]["temp"]}")

 except:
    print("Check the entered field")
    #To easily read and see data in a json file
    #pprint(weatherData)

while end!="y":    
    CurrentWeather()
    end=input("\nwould you like to quit(y/n):")

