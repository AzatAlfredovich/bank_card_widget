import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "my_list, expected_list",
    [
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
    ],
)
def test_filter_by_state(my_list, expected_list):
    assert filter_by_state(my_list) == expected_list


@pytest.mark.parametrize(
    "my_list, sorted_list",
    [
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
    ],
)
def test_sort_by_date(my_list, sorted_list):
    assert sort_by_date(my_list) == sorted_list
