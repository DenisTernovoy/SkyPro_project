from typing import Union

import pandas as pd


def read_csv_file(file_path: str) -> Union[list[dict], None]:
    """Функция для считывания финансовых операций из файла CSV, возвращающая список словарей с транзакциями"""

    try:
        df = pd.read_csv(file_path, delimiter=";")
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Произошла ошибка при попытке считать файл: {e}")
        return None


def read_excel_file(file_path: str) -> Union[list[dict], None]:
    """Функция для считывания финансовых операций из файла Excel, возвращающая список словарей с транзакциями"""

    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Произошла ошибка при попытке считать файл: {e}")
        return None
