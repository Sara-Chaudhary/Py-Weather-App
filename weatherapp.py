import requests
import os

city = input("Enter the name of the city :  ")

url= f"http://api.weatherapi.com/v1/current.json?key=c6c6bf8e142040849cd102933231809&q={city}"

r = requests.get(url)
print(r.text)

# os.system(f"say 'The current weather in {city} is {w} degrees Celcius '")