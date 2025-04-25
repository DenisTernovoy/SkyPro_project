from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    """Функция для маскировки номера"""

    account_param = bank_info.split()
    number = int(account_param[-1])

    match len(account_param[-1]):
        case 16:
            masked_account = " ".join(account_param[:-1]) + " " + get_mask_card_number(number)
        case _:
            masked_account = " ".join(account_param[:-1]) + " " + get_mask_account(number)

    return masked_account


if __name__ == "__main__":
    print(mask_account_card("Счет 35383033474447895560"))
