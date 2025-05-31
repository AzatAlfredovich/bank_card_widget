from typing import Any


def filter_by_state(operation_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, принимающая список словарей и опционально значение для ключа state
     и возвращающая новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list = []
    for item in operation_list:
        if item.get("state") == state:
            new_list.append(item)
    return new_list


def sort_by_date(operation_list: list[dict[str, Any]], reverse_: bool = True) -> list[dict[str, Any]]:
    """Функция, принимающая список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращающая новый список, отсортированный по дате (date)"""
    return sorted(operation_list, key=lambda item: item["date"], reverse=reverse_)


if __name__ == "__main__":
    test_list = [
        {"id": 12, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 34, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 56, "state": "CANCELED", "date": "2017-06-30T02:08:58.425572"},
        {"id": 78, "state": "CANCELED", "date": "2020-06-30T02:08:58.425572"},
    ]
    print(filter_by_state(test_list, "EXECUTED"))
    print(filter_by_state(test_list, "CANCELED"))
    print(sort_by_date(test_list, True))
    print(sort_by_date(test_list, False))
