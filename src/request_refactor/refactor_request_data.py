

def refactor_response(request_result: dict) -> dict[str, str | int]:

    """
    Reordering the country data request result.
    Sets the whole country name as key for the dictionary.
    """

    request_result = request_result["results"]
    key_list = request_result.keys()

    reordered_country_dict = {}

    for key in key_list:
        reordered_country_dict.get(key, "")
        reordered_country_dict[request_result[key]["name"]] = request_result[key]

    return reordered_country_dict


def calculate_exchange_rate(class_widget: object, currency_1: str, currency_2: str) -> list[int]:

    """
    Calculating the exchange rate and returning an 1-dimensional list containing the exchange rate.
    """

    return [value for key, value in class_widget.convertCurrency(currency_1, currency_2).items()]