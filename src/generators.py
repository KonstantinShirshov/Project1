from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция, которая возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


# if __name__ == "__main__":
#     usd_transactions = filter_by_currency(transactions, "USD")
#     for _ in range(2):
#         print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция возвращает действия над счетами"""
    for transaction in transactions:
        yield transaction["description"]


# if __name__ == "__main__":
#     descriptions = transaction_descriptions(transactions)
#     for _ in range(5):
#         print(next(descriptions))


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Функция, которая возвращает номера банковских карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    if len(str(start)) > 16 or len(str(end)) > 16 or start > end or isinstance(start, str) or isinstance(end, str):
        yield ""
    else:
        for i in range(start, end + 1):
            text = (16 - len(str(i))) * "0" + str(i)
            yield " ".join(text[b * 4 : (b + 1) * 4] for b in range(4))


# if __name__ == "__main__":
#     for card_number in card_number_generator(1, 5):
#         print(card_number)
