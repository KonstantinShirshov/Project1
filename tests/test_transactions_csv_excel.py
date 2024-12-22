from unittest.mock import patch

from src.transactions_csv_excel import reading_csv_file, reading_xlsx_file


@patch("pandas.read_csv")
def test_reading_csv_file(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    result = reading_csv_file("data/test_file.csv")
    assert result == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


def test_reading_csv_file_nofile():
    """Функция тестирует reading_csv_file на случай, если файл не найден"""
    assert reading_csv_file("nofile") == []


def test_not_a_list_reading_csv_file():
    """Функция тестирует reading_csv_file на некорректные данные (например, не список)"""
    assert reading_csv_file("../data/transacts.csv") == []


@patch("pandas.read_excel")
def test_reading_xlsx_file(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    result = reading_xlsx_file("data/test_file.xlsx")
    assert result == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


def test_reading_xlsx_file_nofile():
    """Функция тестирует reading_csv_file на случай, если файл не найден"""
    assert reading_xlsx_file("nofile") == []


def test_not_a_list_reading_xlsx_file():
    """Функция тестирует reading_xlsx_file на некорректные данные (например, не список)"""


assert reading_xlsx_file("data/no_list_file") == []
