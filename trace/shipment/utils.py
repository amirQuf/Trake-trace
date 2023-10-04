from trace.shipment.models import Articles
import re
import requests


def extract_zip_code(address: str) -> str:
    """
    Extracts the first 5-digit zip code from the given address.

    Args:
        address (str): The address from which to extract the zip code.

    Returns:
        str: The first 5-digit zip code found in the address. Returns an empty string if no zip code is found.
    """
    zipcode_pattern = r"\b\d{5}\b"
    arg = re.findall(zipcode_pattern, address)
    if arg:
        return arg[0]
    else:
        return ""


def get_all_receiver_zipcode():
    """
    Extracts zip codes from the receiver address of articles.

    Returns:
        list: A list of extracted zip codes.
    """
    zip_codes = []
    articles_list = Articles.objects.all()
    for article in articles_list:
        zip_codes.append(extract_zip_code(article.receiver_address))

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
