import json
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion


def get_operations_data(path: str) -> Any:
    try:
        with open(path, encoding="utf-8") as f:
            try:
                data_json = json.load(f)
            except JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
        return data_json
    except FileNotFoundError:
        print("Файл не найден")
        return []


def transaction_amount(transact: list, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transact["operationAmount"]["currency"]["code"] == currency:
        amount = transact["operationAmount"]["amount"]
    else:
        amount = currency_conversion(transact)
    return amount


# if __name__ == '__main__':
#     path = '../data/operations.json'
#     print(get_operations_data(path))
#     data = get_operations_data(path)
#     transaction_amount(data[0], "RUB")
