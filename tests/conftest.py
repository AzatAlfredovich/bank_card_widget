import pytest


@pytest.fixture
def fixtest_get_date():
    return "2025-05-23T02:26:18.671407"


@pytest.fixture
def fixtest_card_number_generator():
    return "0000 0000 0000 0012"


@pytest.fixture
def fixtest_card_number_generator_range():
    return "Неверно указан диапазон"


@pytest.fixture
def fixtest_search_transaction():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]


@pytest.fixture
def fixtest_process_bank_operations():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]
