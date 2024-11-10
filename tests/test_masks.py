import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("7642211567767987") == "7642 21** **** 7987"


def test_get_mask_account():
    assert get_mask_account("98543355687898542153") == "**2153"
