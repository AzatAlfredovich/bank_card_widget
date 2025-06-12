import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Тесты для фильтрации по валюте "filter_by_currency"


@pytest.mark.parametrize(
    "my_list, filtered_list",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            ["Операций в заданной валюте отсутствуют"],  # USD != RUB
        ),
        (
            [],  # Пустой список
            ["Список транзакций пуст"],
        ),
        (
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {
                        "amount": "43318.34",
                        "currency": {"name": "руб.", "code": "RUB"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                }
            ],
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {
                        "amount": "43318.34",
                        "currency": {"name": "руб.", "code": "RUB"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                }
            ],
        ),
    ],
)
def test_filter_by_currency(my_list, filtered_list):
    result = list(filter_by_currency(my_list, "RUB"))
    assert result == filtered_list


# Тест для генератора, выдающего описания "transaction_descriptions"


@pytest.mark.parametrize(
    "my_list, description",
    [
        ([], "Список транзакций пуст"),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "Описание отсутствует",
        ),
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            "Перевод организации",
        ),
    ],
)
def test_transaction_descriptions(my_list, description):
    assert next(transaction_descriptions(my_list)) == description


# Тесты для генерации номера карты "card_number_generator"


def test_card_number_generator(fixtest_card_number_generator):
    assert next(card_number_generator(12, 20)) == fixtest_card_number_generator


def test_card_number_range(fixtest_card_number_generator_range):
    assert next(card_number_generator(20, 12)) == fixtest_card_number_generator_range
