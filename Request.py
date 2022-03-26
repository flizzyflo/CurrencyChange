
import requests

class RequestCurrency:

    def __init__(self) -> None:
        self.API_KEY= "a8d100711fc77a67b20f"
        self.BASEURL= f"https://free.currconv.com/api/v7/"


    def get_currency_data(self) -> dict:
        """Getting the Base Currency data and unformation about currencies"""

        endpoint = "currencies?apiKey="
        url = f"{self.BASEURL}{endpoint}{self.API_KEY}"
        
        return requests.get(url).json()


    def convert_currency(self, currency_1: str = "USD", currency_2: str = "EUR") -> dict:
        """Converting two currencies, input is currency code of a country currency."""

        endpoint = f"convert?q={currency_1}_{currency_2}&compact=ultra&apiKey="
        url= f"https://free.currconv.com/api/v7/{endpoint}{self.API_KEY}"
        
        return requests.get(url).json()


    def get_country_data(self) -> dict:
        """Getting an overview about all countries and their currencies, currency code, country code."""

        endpoint = f"countries?apiKey={self.API_KEY}"
        url = f"{self.BASEURL}{endpoint}"
        
        return requests.get(url).json()
