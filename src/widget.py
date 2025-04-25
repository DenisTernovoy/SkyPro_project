from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    """Функция для маскировки номера"""

    account_param = bank_info.split()
    number = int(account_param[-1])

    match len(account_param[-1]):
        case 16:
            account_param[-1] = get_mask_card_number(number)
        case _:
            account_param[-1] = get_mask_account(number)

    return " ".join(account_param)


def get_date(user_date: str) -> str:
    """Функция для форматирования даты"""

    formatted_date = user_date.split("-")

    return f"{formatted_date[2][:2]}.{formatted_date[1]}.{formatted_date[0]}"


if __name__ == "__main__":
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(get_date("2024-03-11T02:26:18.671407"))
