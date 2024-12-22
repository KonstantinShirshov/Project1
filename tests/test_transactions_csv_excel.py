from unittest.mock import patch
import pytest
from src.transactions_csv_excel import reading_csv_file, reading_xlsx_file

@patch("pandas.read_csv")
def test_reading_csv_file(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [
        {
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'}
    ]
    result = reading_csv_file("../data/test_file.csv")
    assert result == [
        {
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'}
    ]

def test_reading_csv_file_nofile():
    """Функция тестирует reading_csv_file на случай, если файл не найден"""
    assert reading_csv_file("nofile") == []


def test_not_a_list_reading_csv_file():
    """Функция тестирует reading_csv_file на некорректные данные (например, не список)"""
    assert reading_csv_file("../data/transacts.csv") == []


@patch("builtins.open", new_callable=mock_open,
       read_data='''[{'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z',
                      'amount': 23423.0, 'currency_name': 'Peso', 'currency_code': 'PHP',
                      'from': 'Discover 7269000803370165',
                      'to': 'American Express 1963030970727681',
                      'description': 'Перевод с карты на карту'}]''')
def test_valid_reading_xlsx_file(mock_file: str) -> None:
    """Функция тестирует reading_xlsx_file from src.utils_csv_xlsx на корректный файл с транзакциями"""
    transactions = reading_xlsx_file("data/operations_excel.xlsx")
    assert transactions == [{'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z',
                              'amount': 23423.0, 'currency_name': 'Peso', 'currency_code': 'PHP',
                              'from': 'Discover 7269000803370165',
                              'to': 'American Express 1963030970727681',
                              'description': 'Перевод с карты на карту'}]


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_not_a_list_reading_xlsx_file(mock_file: str) -> None:
    """Функция тестирует reading_xlsx_file from src.utils_csv_xlsx на некорректные данные (например, не список)"""
    not_a_list_transactions = reading_xlsx_file("data/operations_excel.xlsx")
    assert not_a_list_transactions == []

#
@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found_reading_xlsx_file(mock_file: str) -> None:
    """Функция тестирует reading_xlsx_file на случай, если файл не найден"""
    file_not_found_transactions = reading_xlsx_file("data/operations_excel.xlsx")
    assert file_not_found_transactions == []