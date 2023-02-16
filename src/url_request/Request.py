
import requests
from src.settings.Settings import *


class RequestCurrency:

    def __init__(self) -> None:
        self.API_KEY = API_KEY
        self.BASEURL = BASE_URL

    def get_currency_data(self) -> dict[str, str | int]:
        """
        Getting the Base Currency data and unformation about currencies
        """

        endpoint = "currencies?apiKey="
        url = f"{self.BASEURL}{endpoint}{self.API_KEY}"
        
        return requests.get(url).json()

    def convert_currency(self, currency_1: str = "USD", currency_2: str = "EUR") -> dict[str, str | int]:

        """
        Converting two currencies, input is currency code of a country currency.
        """

        endpoint = f"convert?q={currency_1}_{currency_2}&compact=ultra&apiKey="
        url = f"https://free.currconv.com/api/v7/{endpoint}{self.API_KEY}"
        
        return requests.get(url).json()

    def get_country_currency_data(self) -> dict[str, str | int]:
        """Getting an overview about all countries and their currencies, currency code, country code."""

        endpoint = f"countries?apiKey={self.API_KEY}"
        url = f"{self.BASEURL}{endpoint}"
        
        return requests.get(url).json()
