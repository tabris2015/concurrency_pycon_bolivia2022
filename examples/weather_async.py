import asyncio
import time
import aiohttp

API_KEY = "05f65f01f0849a087b905ad802fdbf00"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

CITIES = [
    "Cochabamba",
    "Quito",
    "Salta"
    ]


async def get_city_weather(city):
    url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    async with aiohttp.request("GET", url) as response:
        data = await response.json()
    print(data)


async def main():
    await asyncio.gather(*[get_city_weather(city) for city in CITIES])

if __name__ == '__main__':
    asyncio.run(main())
