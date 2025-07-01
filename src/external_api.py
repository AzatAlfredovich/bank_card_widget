import os

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_convertor(currency: str, amount: float) -> float:
    """Функция, которая обращается к API для получения текущего курса валюты и конвертации"""
    new_currency = "RUB"
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {"to": new_currency, "from": currency, "amount": amount}
    headers = {"apikey": os.getenv("API_KEY_LAYER")}

    response = requests.get(url, headers=headers, params=payload)
    return float(response.json().get("result", 100))


# print(currency_convertor("USD", 100))
# print(type(currency_convertor("USD", 100)))
