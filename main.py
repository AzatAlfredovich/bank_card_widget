from src.masks import get_mask_account, get_mask_card_number  # type: ignore
from src.utils import convertor_to_rubles  # type: ignore
from transactions_csv_read import reading_csv  # type: ignore
from transactions_xlsx_read import reading_xlsx  # type: ignore

# print(get_mask_card_number("1234 1234 1234 123"))
# print(get_mask_card_number("1234 1234 1234 f,du"))
# print(get_mask_card_number("1234 1234 1234 5678"))
#
# print(get_mask_account("1234 1234 1234 1234 567"))
# print(get_mask_account("1234 1234 1234 1234 f,du"))
# print(get_mask_account("1234 1234 1234 1234 5678"))
#
# print(convertor_to_rubles({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "c": "RUB"}}}))
# print(convertor_to_rubles({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}}}))
# print(convertor_to_rubles({"operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}}}))

if __name__ == "__main__":
    # print(reading_csv("data/transactions.csv"))

    print(reading_xlsx("data/transactions_excel.xlsx"))
