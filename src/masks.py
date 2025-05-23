from typing import Union


# Функция теперь имеет аннотацию по типам - какой на входе и выходе
def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция, принимающая на вход номер карты и возвращающая маску номера, показывая 4 первые и 4 последние цифры"""

    card_number = card_number.replace(" ", "")
    masked_card_number = " ".join(card_number[i : i + 4] for i in range(0, len(card_number), 4))
    masked_card_number_list = list(masked_card_number)

    for i in range(len(masked_card_number_list)):
        if 7 <= i <= 13 and masked_card_number_list[i] != " ":
            masked_card_number_list[i] = "*"

    masked_card_number = "".join(masked_card_number_list)
    return masked_card_number


def get_mask_account(account_number: Union[str]) -> str:
    """Функция, принимающая на вход номер аккаунта и возвращающая маску номера, 4 последние цифры, перед которыми **"""
    account_number_united = account_number.replace(" ", "")
    number_mask = str(account_number_united[-4:])
    return f"**{number_mask}"
