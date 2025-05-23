from mypy.types import Union

from src.masks import get_mask_account, get_mask_card_number


# Функция теперь имеет аннотацию по типам - какой на входе и выходе
def mask_account_card(card_or_account_number: Union[str]) -> str:
    """Функция, принимающая на вход номер карты или счета, возвращающая маску
    с частичным номером карты или последними 4 цифрами номера счета"""
    if "счет" in card_or_account_number.lower() or "счёт" in card_or_account_number.lower():
        return f"Счет {get_mask_account(card_or_account_number)}"
    else:
        masked_card_number = card_or_account_number.replace(
            card_or_account_number[-16:], get_mask_card_number(card_or_account_number[-16:])
        )
        return masked_card_number


def get_date(current_date: Union[str]) -> str:
    """Функция, принимающая на вход строку в формате, возвращающая чистую дату"""
    new_date = []
    new_date.append(current_date[8:10])
    new_date.append(current_date[5:7])
    new_date.append(current_date[:4])
    return ".".join(new_date)
