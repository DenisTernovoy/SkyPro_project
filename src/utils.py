import json
import logging
import os
import pathlib

base_path = pathlib.Path(__file__).resolve().parent.parent
directory = base_path / "logs/utils.log"

logger = logging.getLogger("utils")
logger_handler = logging.FileHandler(directory, encoding="utf-8", mode="w")
logger_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)
logger.setLevel("DEBUG")


def get_transactions_info(file_path: str) -> list:
    """Функция возвращает список словарей с данными о финансовых транзакциях из файла в формате JSON.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    logger.debug("Запуск функции get_transactions_info")

    if not os.path.isfile(file_path):
        logger.info("Файл в указанной директории не существует")
        return []

    with open(file_path, encoding="utf-8") as file:
        logger.debug("Вызов контекстного менеджера")
        try:
            data = json.load(file)
            logger.info("Чтение JSON-файла")
            if isinstance(data, list):
                logger.info("Возврат содержимого JSON-файла")
                return data
            else:
                logger.info("JSON-файл пустой")
                return []
        except json.JSONDecodeError:
            logger.error("Ошибка в декодировании JSON-файла")
            return []
