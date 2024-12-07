import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
headers = {"apikey": api_key}


def currency_conversion(transaction: Any) -> Any:
    """Функция конвертации"""
    amout = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    response = requests.get(url, headers=headers)
    result = response.json()
    return result["result"]
