import requests
import json
import pyttsx3
engine = pyttsx3.init()

engine.say("Which City Temperature you want to know ")
engine.runAndWait()
city=input("Which City Temperature you want to know ")

url=f"https://api.weatherapi.com/v1/current.json?key=8a81b139372e4f49a06165215240311&q={city}"
weatherData= requests.get(url)

weather_Dictionary=weatherData.json()

temperature_celcius=weather_Dictionary["current"]["temp_c"]
weather_condition=weather_Dictionary["current"]["condition"]["text"]
weather=f"the temperature of {city} is {temperature_celcius}°C and the weather condition is {weather_condition}"
print(weather)
engine.say(weather)
engine.runAndWait()