import pytest


@pytest.fixture
def fixtest_get_mask_card_number():
    return [
        ("7000 7922 8960 6361" == "7000 79** **** 6361"),
        ("7000792289606361" == "7000 79** **** 6361"),
        ("12" == "0000 00** **** 0000"),
        "" == "0000 00** **** 0000",
    ]


@pytest.fixture
def fixtest_get_mask_account():
    return [
        ("7000792289606361" == "**6361"),
        ("7000 7922 8960 6361" == "**6361"),
        ("7922 8960 6361" == "**0000"),
        ("" == "**0000"),
    ]


@pytest.fixture
def fixtest_filter_by_state():
    return [
        (
            [
                {"id": 12, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 34, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 56, "state": "CANCELED", "date": "2017-06-30T02:08:58.425572"},
                {"id": 78, "state": "CANCELED", "date": "2020-06-30T02:08:58.425572"},
            ],
            [
                {"id": 12, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 34, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ]


@pytest.fixture
def fixtest_sort_by_date():
    return [
        (
            [
                {"id": 12, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 34, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 56, "state": "CANCELED", "date": "2017-06-30T02:08:58.425572"},
                {"id": 78, "state": "CANCELED", "date": "2020-06-30T02:08:58.425572"},
            ],
            [
                {"id": 78, "state": "CANCELED", "date": "2020-06-30T02:08:58.425572"},
                {"id": 12, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 34, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 56, "state": "CANCELED", "date": "2017-06-30T02:08:58.425572"},
            ],
        )
    ]


@pytest.fixture
def fixtest_mask_account_card():
    return [
        ("Счет 73654108430135874315", "Счет **4315"),
        ("счёт 73654108430135874306", "Счет **4306"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ]


@pytest.fixture
def fixtest_get_date():
    return ["2025-05-23T02:26:18.671407", "23.05.2025"]
