from src.widget import get_date


def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    new_list = []

    for i in list_dict:
        if isinstance(i, dict):
            if "state" in i:
                if i["state"] == state:
                    new_list.append(i)
    return new_list


def sort_by_date(list_dict: list[dict], sort_decrease: bool = True) -> list[dict]:
    """Функция принимает список словарей и возвращает отсортированный по дате список согласно параметру sort_mode,
    задающему порядок сортировки"""

    new_list = []

    for i in list_dict:
        if isinstance(i, dict):
            if "date" in i:
                try:
                    get_date(i["date"])
                    new_list.append(i)
                except ValueError:
                    pass

    return sorted(new_list, key=lambda x: x["date"], reverse=sort_decrease)
