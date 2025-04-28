import datetime as dt
import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    """Функция для маскировки номера"""

    if bank_info:
        account_param = bank_info.split()
        number = account_param[-1]

        if len(account_param) >= 2:
            if account_param[0] == "Счет":
                account_param[-1] = get_mask_account(number)
            elif account_param[0] in ("Maestro", "MasterCard", "Visa"):
                account_param[-1] = get_mask_card_number(number)
            else:
                raise ValueError("Некорректный тип карты или счета")
            return " ".join(account_param)

    raise ValueError("Укажите тип и номер карты или счета")


def get_date(user_date: str) -> str:
    """Функция для форматирования даты"""

    if user_date:
        res = re.match(r"(\d{4})-(\d{2})-(\d{2})T", user_date[:11])

        if res:
            try:
                dt.datetime.strptime(f"{res.group(3)}.{res.group(2)}.{res.group(1)}", "%d.%m.%Y")
            except Exception:
                raise ValueError("Введен некорректный формат даты")

            return f"{res.group(3)}.{res.group(2)}.{res.group(1)}"
        else:
            raise ValueError("Введен некорректный формат даты")

    raise ValueError("Отсутствует дата для форматирования")
