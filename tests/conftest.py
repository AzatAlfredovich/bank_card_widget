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
