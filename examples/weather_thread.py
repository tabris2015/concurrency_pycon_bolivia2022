import json
from threading import Thread
import time
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
    thread_list = []
    for city in CITIES:
        city_th = Thread(target=get_city_weather, args=(city,))
        thread_list.append(city_th)
        city_th.start()

    for i, thread in enumerate(thread_list):
        print(f"Before joining th{i}")
        thread.join()
        print(f"th{i} done")


if __name__ == '__main__':
    main()
