import textwrap
from typing import Generator


def filter_by_currency(list_dicts: list[dict], currency: str) -> filter:
    return filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, list_dicts)


def transaction_descriptions(list_dicts: list[dict]) -> Generator:
    i = 0
    while True:
        yield list_dicts[i]["description"]
        i += 1


def card_number_generator(start: int, end: int) -> Generator:
    while start != end + 1:
        yield " ".join(textwrap.wrap(f"{start:016}", 4))
        start += 1
