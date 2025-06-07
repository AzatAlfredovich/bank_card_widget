import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000 7922 8960 6365", "7000 79** **** 6365"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("123", "Введен некорректный номер карты"),
        ("", "Введен некорректный номер карты"),
        ("abcd efgh qwer asdf", "Номер карты должен состоять только из цифр"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "Введен некорректный номер счета"),
        ("70 00 79 22 89 60 63 61", "Введен некорректный номер счета"),
        ("7000 7922 8960 6361", "Введен некорректный номер счета"),
        ("123", "Введен некорректный номер счета"),
        ("7000 7922 8960 6361 1234", "**1234"),
        ("абсв 7922 8960 6361 1234", "Номер счета должен состоять только из цифр"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
