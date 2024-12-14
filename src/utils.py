import json
import logging
from json import JSONDecodeError
from typing import Any
from src.external_api import currency_conversion


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename="../logs/utils.log",
    encoding="utf-8",
    filemode="w",
)
get_operations_data_logger = logging.getLogger()
transaction_amount_logger = logging.getLogger()


def get_operations_data(path: str) -> Any:
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        get_operations_data_logger.info("Открываю вайл с транзакциями")
        with open(path, encoding="utf-8") as f:
            try:
                data_json = json.load(f)
            except JSONDecodeError:
                get_operations_data_logger.error("Ошибка декодирования файла")
                print("Ошибка декодирования файла")
                return []
        get_operations_data_logger.info("Создан список словарей с данными о финансовых транзакциях")
        return data_json
    except FileNotFoundError:
        get_operations_data_logger.error("Файл не найден")
        print("Файл не найден")
        return []


def transaction_amount(transact: list, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transact["operationAmount"]["currency"]["code"] == currency:
        amount = transact["operationAmount"]["amount"]
        transaction_amount_logger.info("Код валюты  в транзакции RUB")
    else:
        amount = currency_conversion(transact)
        transaction_amount_logger.info("Код валюты  в транзакции не RUB, произведена конвертация")
    return amount


if __name__ == "__main__":
    path = "../data/operations.json"
    # print(get_operations_data(path))
    data = get_operations_data(path)
    transaction_amount(data[0], "RUB")
