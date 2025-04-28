import textwrap
from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""

    if isinstance(card_number, int):
        card_number = str(card_number)

    if len(card_number) == 16 and card_number.isdigit():
        return " ".join(textwrap.wrap(f"{card_number[:6]}******{card_number[-4:]}", 4))
    else:
        raise ValueError("Номер банковской карты должен состоять из 16-ти цифровых символов")


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функцию маскировки номера банковского счета"""

    if isinstance(account_number, int):
        account_number = str(account_number)

    if len(account_number) == 20 and account_number.isdigit():
        return f"**{str(account_number)[-4:]}"
    else:
        raise ValueError("Номер банковского счета должен состоять из 20-ти цифровых символов")
