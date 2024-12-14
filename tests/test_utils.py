import os
from unittest.mock import patch

import pytest

from src.utils import get_operations_data, transaction_amount


@pytest.fixture
def path():
    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    return path_to_file


@pytest.fixture
def path_empty_list():
    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operation_1.json")
    return path_to_file


@pytest.fixture
def path_mistake_json():
    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations_2.json")
    return path_to_file


@pytest.fixture
def transact():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def transact_1():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_get_operations_data_nofile():
    assert get_operations_data("nofile") == []


def test_get_operations_data(path):
    assert get_operations_data(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_get_operations_data_empty_list(path_empty_list):
    assert get_operations_data(path_empty_list) == []


def test_get_operations_data_mistake_json(path_mistake_json):
    assert get_operations_data(path_mistake_json) == []


def test_transaction_amount(transact):
    assert transaction_amount(transact) == "31957.58"


@patch("src.utils.currency_conversion")
def test_transaction_amount_non_rub(mock_currency_conversion, transact_1):
    mock_currency_conversion.return_value = 2000.0
    assert transaction_amount(transact_1) == 2000.0
