import pytest

from src.masks import get_mask_account, get_mask_card_number

# def test_get_mask_card_number():
#     assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"
#     assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
#
#
# def test_get_mask_account():
#     assert get_mask_account("7000792289606361") == "**6361"
#     assert get_mask_account("70 00 79 22 89 60 63 61") == "**6361"
#     assert get_mask_account("7000 7922 8960 6361") == "**6361"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000 7922 8960 6365", "7000 79** **** 6365"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("123", "0000 00** **** 0000"),
        ("", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "**0000"),
        ("70 00 79 22 89 60 63 61", "**0000"),
        ("7000 7922 8960 6361", "**0000"),
        ("123", "**0000"),
        ("", "**0000"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
