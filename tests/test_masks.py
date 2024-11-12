import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def numbers_of_card():
    return "7000792289606361"


def test_get_mask_card_number(numbers_of_card):
    assert get_mask_card_number(numbers_of_card) == "7000 79** **** 6361"


@pytest.mark.parametrize("account_numbers, expected", [("98543355687898542153", "**2153"),
                                                       ("73654108430135874305", "**4305"),
                                                       ("43434434343454548779", "**8779")])


def test_get_mask_account(account_numbers, expected):
    assert get_mask_account(account_numbers) == expected
