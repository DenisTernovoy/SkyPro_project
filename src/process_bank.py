import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    filtered_arrange = []
    for i in data:
        if re.search(search.lower(), i["description"].lower()):
            filtered_arrange.append(i)

    return filtered_arrange


def process_bank_operations(data: list[dict], categories: list) -> dict:
    operations = []
    for i in data:
        if i["description"].lower() in list(map(str.lower, categories)):
            operations.append(i["description"])
    result = Counter(operations)

    return dict(result)
