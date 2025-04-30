import textwrap
from typing import Any, Generator


def filter_by_currency(list_dicts: list[dict], currency: str) -> Any:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    try:
        iter_object = list(filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, list_dicts))
    except (TypeError, KeyError):
        iter_object = []

    return iter(iter_object)


def transaction_descriptions(list_dicts: list[dict]) -> Generator:
    """Функция-генератор, поочередно возвращающая описание банковских транзакций"""

    i = 0

    if all("description" in i for i in list_dicts):
        while i != len(list_dicts):
            yield list_dicts[i]["description"]
            i += 1


def card_number_generator(start: int, end: int) -> Generator:
    """Функция-генератор, поочередно возвращающий номера банковских карт в диапазоне от start до end"""

    while start != end + 1:
        yield " ".join(textwrap.wrap(f"{start:016}", 4))
        start += 1
