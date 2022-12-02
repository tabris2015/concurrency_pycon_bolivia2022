import json
import requests


API_KEY = "05f65f01f0849a087b905ad802fdbf00"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

CITIES = [
    "Cochabamba",
    "Quito",
    "Salta"
    ]


def get_city_weather(city):
    url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    print(data)


def main():
    for city in CITIES:
        get_city_weather(city)


if __name__ == '__main__':
    main()
