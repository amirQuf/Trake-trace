from .models import Shipment, Article
from typing import List
from .utils import extract_zip_code
from django.core.cache import cache


def retrieve_all_shipments() -> List[Shipment]:
    """
    Retrieve a list of all shipments.

    Returns:
        List[Shipment]: A list of all shipment objects.
    """
    return Shipment.objects.all()


def retrieve_shipment(shipment_id: int) -> Shipment:
    """
    Retrieve a specific shipment based on its ID.

    Args:
        shipment_id (int): The ID of the shipment to retrieve.

    Returns:
        Shipment: The shipment object corresponding to the given ID.
    """
    return Shipment.objects.get(id=shipment_id)


def retrieve_all_articles() -> List[Article]:
    """
    Retrieve a list of all articles.

    Returns:
        List[Article]: A list of all article objects.
    """
    return Article.objects.all()


def retrieve_article(article_id: int) -> Article:
    """
    Retrieve a specific article based on its ID.

    Args:
        article_id (int): The ID of the article to retrieve.

    Returns:
        Article: The article object corresponding to the given ID.
    """
    return Article.objects.get(id=article_id)


def get_weather(address: str) -> str:
    """
    Retrieves weather information for a given address.

    This function uses the provided address to extract the zip code and then retrieves weather
    information associated with that zip code from the cache.

    Args:
        address (str): The address for which to retrieve weather information.

    Returns:
        str: The weather information for the given address based on the associated zip code.
             Returns an empty string if no weather information is found for the zip code.
    """
    zip_code = extract_zip_code(address)
    weather = cache.get(zip_code)
    return weather
