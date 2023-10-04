from celery import shared_task
from trace.shipment.models import Articles
import re
import requests
from django.core.cache import cache


def get_all_receiver_zipcode():
    zip_codes = []
    zipcode_pattern = r"\b\d{5}\b"
    q = Articles.objects.all()
    for articles in q:
        arg = re.findall(zipcode_pattern, Articles.receiver_address)
        zip_codes.append(arg[0])
    return zip_codes


def weather_api_call(zipcode: str) -> str:
    API_KEY = ""
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + zipcode + "&appid=" + API_KEY
    response = requests.get(URl)
    if response.status_code == 200:
        data = response.json()
        return data["weather"]
    else:
        # Handle API error
        return {"error": "Unable to fetch weather information"}


def get_weathers():
    zip_codes = get_all_receiver_zipcode()
    for zipcode in zip_codes:
        weather = weather_api_call(zipcode)
        cached_weather_info = cache.get(zipcode)
        if not cached_weather_info:
            cache.set(zip_codes, weather)
