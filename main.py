from generators import filter_by_currency, transaction_descriptions
from processing import filter_by_state, sort_by_date
from transaction_search import search_transaction
from transactions_csv_read import reading_csv
from transactions_xlsx_read import reading_xlsx
from utils import open_json

print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями!
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файл""")
user_input_first = input("Выберите необходимый пункт меню: ")

if user_input_first == "1":
    print("Выбран JSON-файл для обработки")
    operation_list = open_json("data/operations.json")
elif user_input_first == "2":
    print("Выбран CSV-файл для обработки")
    operation_list = reading_csv("data/transactions.csv")
else:
    print("Выбран XLSX-файл для обработки")
    operation_list = reading_xlsx("data/transactions_excel.xlsx")

print("""Необходимо выполнить фильтрацию по статусу. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
user_input_status = input("Введите статус: ")
filtered_by_state_list = []
while True:
    if user_input_status.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        print("""Статус ошибочный! Введите доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        user_input_status = input("Введите статус: ")
        continue
    else:
        filtered_by_state_list = filter_by_state(operation_list, user_input_status.upper())
        print(f"Операции отфильтрованы по статусу - {user_input_status.upper()}")
        break
print("Отсортировать операции по дате? Да/Нет")
input_sort_by_date = input("Сортируем? ")
if input_sort_by_date.lower()=="да":
    print("Отсортировать по возрастанию или по убыванию? 1/2")
    input_sort_by_date_= input("Сортируем? ")
    if input_sort_by_date_=="1":
        sort_by_date(filtered_by_state_list, False)
    else:
        sort_by_date(filtered_by_state_list)
else:
    pass

print("Выводить только рублевые транзакции? Да/Нет")
input_filter_by_currency = input("")
if input_filter_by_currency.lower=="да":
    filter_by_currency(filtered_by_state_list, "RUB")
else:
    currency_input = input("Введите валюту, по которой список сортируем: ")
    filter_by_currency(filtered_by_state_list, currency_input.upper())

print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
input_word_filter = input("")
if input_word_filter.lower() == "да":
    input_word_search = input("Введите слово или ряд букв для поиска: ")
    search_transaction(filtered_by_state_list, input_word_search)
else:
    pass

print("Распечатываю итоговый список транзакций...")
print("Всего банковских операций в выборке:")
