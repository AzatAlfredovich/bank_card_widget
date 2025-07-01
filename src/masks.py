import logging
from typing import Union

logger = logging.getLogger("masks_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks_log.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# Функция теперь имеет аннотацию по типам - какой на входе и выходе
def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция, принимающая на вход номер карты и возвращающая маску номера,
    не показывая часть, но показывая 4 последние цифры"""
    logger.info(f"Маскируем номер карты {card_number}")
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        logger.error("Ошибка - номер карты менее 16 символов")
        return "Введен некорректный номер карты"
    elif not card_number.isdigit():
        logger.error("Ошибка - номер карты состоит не только из цифр")
        return "Номер карты должен состоять только из цифр"
    masked_card_number = " ".join(card_number[i : i + 4] for i in range(0, len(card_number), 4))
    masked_card_number_list = list(masked_card_number)

    for i in range(len(masked_card_number_list)):
        if 7 <= i <= 13 and masked_card_number_list[i] != " ":
            masked_card_number_list[i] = "*"

    masked_card_number = "".join(masked_card_number_list)
    logger.info("Номер карты замаскирован")
    return masked_card_number


def get_mask_account(account_number: Union[str]) -> str:
    """Функция, принимающая на вход номер аккаунта и возвращающая маску номера,
    4 последние цифры, перед которыми **"""
    logger.info(f"Маскируем номер счета {account_number}")
    account_number_united = account_number.replace(" ", "")
    if len(account_number_united) != 20:
        logger.error("Ошибка - номер счета менее 20 символов")
        return "Введен некорректный номер счета"
    elif not account_number_united.isdigit():
        logger.error("Ошибка - номер счета состоит не только из цифр")
        return "Номер счета должен состоять только из цифр"
    number_mask = str(account_number_united[-4:])
    logger.info(f"Номер счета замаскирован - **{number_mask}")
    return f"**{number_mask}"
