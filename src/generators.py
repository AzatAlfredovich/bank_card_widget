from typing import Generator, Iterator


def filter_by_currency(transaction_list: list, currency: str) -> Iterator:
    """Функция, фильтрующая транзакции по заданной валюте и возвращающая итератор"""
    if not transaction_list:
        yield "Список транзакций пуст"
    else:
        found = False
        for transaction in transaction_list:
            amount_data = transaction.get("operationAmount")
            if amount_data and amount_data.get("currency"):
                current_currency = amount_data["currency"]["code"]
                if current_currency == currency:
                    found = True
                    yield transaction
        if not found:
            yield "Операций в заданной валюте отсутствуют"


def transaction_descriptions(transaction_list: list) -> Iterator:
    """Генератор, поочередно выдающий описание транзакции"""
    if transaction_list:
        for transaction in transaction_list:
            if transaction.get("description"):
                yield transaction["description"]
            else:
                yield "Описание отсутствует"
    else:
        yield "Список транзакций пуст"


def card_number_generator(start: int, end: int) -> Generator:
    """Генератор номеров карт в заданном диапазоне"""
    start_int = int(str(start).replace(" ", ""))
    end_int = int(str(end).replace(" ", ""))
    if start_int < end_int + 1:
        for i in range(start_int, end_int + 1):
            formatted_number = str(i).zfill(16)
            formatted_number = (
                formatted_number[:4]
                + " "
                + formatted_number[4:8]
                + " "
                + formatted_number[8:12]
                + " "
                + formatted_number[12:]
            )
            yield formatted_number
    else:
        yield "Неверно указан диапазон"
