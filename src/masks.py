import textwrap


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""

    masked_number = str(card_number)[:6] + "*" * 6 + str(card_number)[-4:]
    return " ".join(textwrap.wrap(masked_number, 4))


def get_mask_account(account_number: int) -> str:
    """Функцию маскировки номера банковского счета"""

    masked_account_number = "**" + str(account_number)[-4:]
    return masked_account_number


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
