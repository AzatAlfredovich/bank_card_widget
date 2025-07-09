import json
import logging

from src.external_api import currency_convertor

logger = logging.getLogger("utils_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils_log.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_json(path: str) -> list:
    """Функция, которая преобразует JSON-объект в Python-объект"""
    try:
        logger.info("Преобразовываем JSON-файл в объект Python")
        with open(path, "r", encoding="utf-8") as f:
            logger.info("Файл преобразован")
            return list(json.load(f))
    except json.JSONDecodeError:
        logger.error("Ошибка форматирования JSON-файла : json.JSONDecodeError")
        return []
    except Exception:
        logger.error("Ошибка форматирования JSON-файла : Exception")
        return []


def convertor_to_rubles(operation: dict) -> float:
    """Функция, которая конвертирует валюту в рубли"""
    logger.info("Конвертируем валюту и считаем сумму")
    try:
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            logger.info(f"Сумма подсчитана - {operation["operationAmount"]["amount"]}")
            return float(operation["operationAmount"]["amount"])
        else:
            operation_currency = operation["operationAmount"]["currency"]["code"]
            operation_amount = operation["operationAmount"]["amount"]
            logger.info(f"Сумма подсчитана - {currency_convertor(operation_currency, operation_amount)}")
            return float(currency_convertor(operation_currency, operation_amount))
    except Exception:
        logger.error("Ошибка, обнуляем сумму и завершаем работу")
        return 0.0


# print(
#     convertor_to_rubles(
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#         }
#     )
# )
