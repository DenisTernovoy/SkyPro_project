from typing import Any

import pandas

from src.generators import filter_by_currency
from src.process_bank import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.read_data import read_csv_file, read_excel_file
from src.utils import get_transactions_info
from src.widget import get_date, mask_account_card


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_input = input()

    while True:
        if user_input not in "123" or len(user_input) >= 2:
            print("Введите цифру 1-3, обозначающую формат файла для обработки")
            user_input = input()
        else:
            formats = ["JSON", "CSV", "XLSX"]
            choice_format = formats[int(user_input) - 1]
            print(f"Для обработки выбран {choice_format}-файл.")

            if choice_format == "JSON":
                transactions: Any = get_transactions_info("./data/operations.json")
            elif choice_format == "CSV":
                transactions = read_csv_file("./data/transactions.csv")
            elif choice_format == "XLSX":
                transactions = read_excel_file("./data/transactions_excel.xlsx")

            break

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    user_input = input().upper()
    status = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        if user_input.upper() in status:
            print(f"Операции отфильтрованы по статусу '{user_input}'")
            transactions = filter_by_state(transactions, user_input)
            break
        else:
            print(f"Статус операции '{user_input}' недоступен.")

            print("Введите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            user_input = input()

    print("Отсортировать операции по дате? Да/Нет")

    user_input = input().lower()

    while True:
        if user_input in ["да", "нет"]:
            break
        else:
            print("Отсортировать операции по дате? Да/Нет")
            user_input = input().lower()

    if user_input == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input = input().lower()

        while True:
            if user_input in ["по возрастанию", "по убыванию"]:
                match user_input:
                    case "по возрастанию":
                        transactions = sort_by_date(transactions, False)
                    case _:
                        transactions = sort_by_date(transactions)
                break
            else:
                print("Отсортировать по возрастанию или по убыванию?")
                user_input = input().lower()

    print("Выводить только рублевые транзакции? Да/Нет")
    user_input = input().lower()

    while True:
        if user_input in ["да", "нет"]:
            if user_input == "да":
                transactions = list(filter_by_currency(transactions, "RUB"))
            break
        else:
            print("Выводить только рублевые транзакции? Да/Нет")
            user_input = input().lower()

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input = input().lower()

    while True:
        if user_input in ["да", "нет"]:
            if user_input == "да":
                filter_word = input("Введите слово для фильтрации: ")
                transactions = process_bank_search(transactions, filter_word)
            break
        else:
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            user_input = input().lower()

    print("Распечатываю итоговый список транзакций...")

    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")

        for i in transactions:
            print(f"{get_date(i["date"])} {i["description"]}")
            print(i)
            if "from" in i:
                if pandas.notna(i["from"]):
                    print(f"{mask_account_card(i['from'])} -> {mask_account_card(i['to'])}")
                else:
                    print(mask_account_card(i["to"]))
            else:
                print(mask_account_card(i["to"]))

            if "operationAmount" in i:
                print(f'Сумма: {i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}')
            else:
                print(f'Сумма: {i["amount"]} {i["currency_name"]}')
            print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
