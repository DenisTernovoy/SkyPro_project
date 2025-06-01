import pandas as pd


def read_csv_file(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из файла CSV, возвращающая список словарей с транзакциями"""

    with open(file_path, encoding="utf-8") as file:
        df = pd.read_csv(file)
        return df.to_dict(orient="records")
