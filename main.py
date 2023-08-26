
import requests

#
api_key = input("Enter Your API key: ")

city = input("Enter city name: ")

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

response = requests.get(url)

if response.status_code != 200:
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Temperature: {temp} K")
    print(f"Description: {desc}")
else:
    print("Invalid API Key")
