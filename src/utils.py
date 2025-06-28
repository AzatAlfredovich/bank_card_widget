import json
from external_api import currency_convertor


def open_json(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        except Exception:
            return []


# print(open_json("../data/operations.json"))


def convertor_to_rubles(operation: dict) -> float:
    if operation:
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return float(operation["operationAmount"]["amount"])
        else:
            operation_currency = operation["operationAmount"]["currency"]["code"]
            operation_amount = operation["operationAmount"]["amount"]
            return float(currency_convertor(operation_currency, operation_amount))
    return 0.0


print(convertor_to_rubles(open_json("../data/operations.json")[5]))
