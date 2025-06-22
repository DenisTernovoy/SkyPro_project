import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""

    filtered_arrange = []
    for i in data:
        if re.search(search.lower(), i["description"].lower()):
            filtered_arrange.append(i)

    return filtered_arrange


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    operations = []
    for i in data:
        if i["description"].lower() in list(map(str.lower, categories)):
            operations.append(i["description"])
    result = Counter(operations)

    return dict(result)
