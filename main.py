
import requests

#
api_key = "8c89d38415e7cd7cbcf6f0ee694df251"

city = input("Enter city name: ")

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

response = requests.get(url)

if response.json()["cod"] == 200:
    data = response.json()
    temp = round(data["main"]["temp"]-273)
    desc = data["weather"][0]["description"]
    print(f"Temperature: {temp} C")
    print(f"Description: {desc}")
else:
    print("Invalid API Key")
