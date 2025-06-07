import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 73654108430135874315", "Счет **4315"),
        ("счёт 73654108430135874306", "Счет **4306"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected", [("2025-05-23T02:26:18.671407", "23.05.2025"), ("2023-04-21T02:26:18.671407", "21.04.2023")]
)
def test_get_date(value, expected):
    assert get_date(value) == expected

def test_get_date_fixture(fixtest_get_date):
    assert get_date(fixtest_get_date) == "23.05.2025"