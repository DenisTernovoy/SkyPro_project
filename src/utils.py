import json
import os


def get_transactions_info(file_path: str) -> list:
    """Функция возвращает список словарей с данными о финансовых транзакциях из файла в формате JSON.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    if not os.path.isfile(file_path):
        return []

    with open(file_path, encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []
