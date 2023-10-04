from celery import shared_task
from .utils import get_all_receiver_zipcode, WeatherAPICaller
from django.core.cache import cache


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
