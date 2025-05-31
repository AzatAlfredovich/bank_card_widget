from typing import  Any

def filter_by_state(operation_list: list[dict[str, Any]], state: str ='EXECUTED') -> list[dict[str, Any]] :
    """Функция, принимающая список словарей и опционально значение для ключа state
 и возвращающая новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению."""
    new_list=[]
    for item in operation_list:
        if item.get('state') == state:
            new_list.append(item)
    return new_list

def sort_by_date(operation_list:  list[dict[str, Any]], reverse_ : bool= True) -> list[dict[str, Any]] :
    """Функция, принимающая список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращающая новый список, отсортированный по дате (date)"""
    return sorted(operation_list, key=lambda item: item['date'], reverse = reverse_)