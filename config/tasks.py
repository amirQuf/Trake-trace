from celery import shared_task
from trace.shipment.models import Articles
import re
import requests
from django.core.cache import cache


def get_all_receiver_zipcode():
    """
    Extracts zip codes from the receiver address of articles.

    Returns:
        list: A list of extracted zip codes.
    """
    zip_codes = []
    zipcode_pattern = r"\b\d{5}\b"
    articles_list = Articles.objects.all()
    for articles in articles_list:
        arg = re.findall(zipcode_pattern, Articles.receiver_address)
        if arg:
            zip_codes.append(arg[0])

    return zip_codes


class WeatherAPICaller:
    def __init__(self, api_key):
        """
        Initializes the WeatherAPICaller with the API key.

        Args:
            api_key (str): The API key for accessing the weather API.
        """
        self.API_KEY = api_key
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    def call(self, zipcode: str) -> dict:
        """
        Calls the weather API to retrieve weather information for a given zip code.

        Args:
            zipcode (str): The zip code for which weather information is requested.

        Returns:
            dict: Weather information for the specified zip code.
        """
        URL = f"{self.BASE_URL}q={zipcode}&appid={self.API_KEY}"
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()
            return data.get("weather", [])
        else:
            return {"error": f"Unable to fetch weather information for {zipcode}"}


@shared_task
def get_weathers(api: WeatherAPICaller):
    """
    Retrieves weather information for a list of zip codes and caches the data.

    Args:
        api (WeatherAPICaller): An instance of WeatherAPICaller to call the weather API.
    """
    zip_codes = get_all_receiver_zipcode()
    for zipcode in zip_codes:
        # Call the Weather API using the provided API caller
        weather = api.call(zipcode)
        # Cache the weather information
        cache.set(zipcode, weather)
