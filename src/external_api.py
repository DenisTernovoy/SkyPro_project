import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции рублях"""

    if not isinstance(transaction, dict) or transaction == {}:
        raise ValueError("Некорректный формат транзакции")

    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
    except KeyError:
        raise ValueError("Некорректный формат транзакции")

    if currency == "USD" or currency == "EUR":

        url = "https://api.apilayer.com/exchangerates_data/convert"

        headers = {"apikey": API_KEY}
        params = {"from": transaction["operationAmount"]["currency"]["code"], "to": "RUB", "amount": amount}

        response = requests.get(url, headers=headers, params=params)

        return float(response.json()["result"])
    else:
        return float(transaction["operationAmount"]["amount"])
