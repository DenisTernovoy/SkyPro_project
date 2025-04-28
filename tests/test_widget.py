import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def account() -> str:
    return "Счет **5560"


@pytest.fixture
def card() -> str:
    return "Visa Platinum 8990 92** **** 5229"


@pytest.mark.parametrize("number", ["Счет 35383033474447895560", "Счет 11112222333344445560"])
def test_mask_account_card_account(number: str, account: str) -> None:
    assert mask_account_card(number) == account


def test_mask_account_card_card(card: str) -> None:
    assert mask_account_card("Visa Platinum 8990922113665229") == card


@pytest.mark.parametrize("bank_info", ["8990922113665229", ""])
def test_mask_account_card_invalid(bank_info: str) -> None:
    with pytest.raises(ValueError) as e:
        mask_account_card(bank_info)

    assert str(e.value) == "Укажите тип и номер карты или счета"


def test_mask_account_card_invalid_type() -> None:
    with pytest.raises(ValueError) as e:
        mask_account_card("МИР 4226922113665229")

    assert str(e.value) == "Некорректный тип карты или счета"


@pytest.fixture
def date() -> str:
    return "11.03.2024"


def test_get_date(date: str) -> None:
    assert get_date("2024-03-11T02:26:18.671407") == date


@pytest.mark.parametrize(
    "dates",
    [
        "20-03-11T02:26:18.671407",
        "2024-03-222T02:26:18.671407",
        "2024-031-11T02:26:18.671407",
        "2024-02-30T02:26:18.671407",
    ],
)
def test_get_date_invalid_dates(dates: str) -> None:
    with pytest.raises(ValueError) as e:
        get_date(dates)

    assert str(e.value) == "Введен некорректный формат даты"


def test_get_date_invalid() -> None:
    with pytest.raises(ValueError) as e:
        get_date("")

    assert str(e.value) == "Отсутствует дата для форматирования"
