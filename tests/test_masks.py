from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "numbers, expected", [(1111_2222_3333_4444, "1111 22** **** 4444"), ("1111222244446666", "1111 22** **** 6666")]
)
def test_get_mask_card_number(numbers: Union[int, str], expected: str) -> None:
    assert get_mask_card_number(numbers) == expected


@pytest.mark.parametrize(
    "number", [1111_2222_3333_4444_5555, 1111_2222_3333, "1111_2222_3333_4444", "111122223333aaaa", ""]
)
def test_get_mask_card_number_invalid_number(number: Union[int, str]) -> None:
    with pytest.raises(ValueError) as e:
        get_mask_card_number(number)

    assert str(e.value) == "Номер банковской карты должен состоять из 16-ти цифровых символов"


@pytest.fixture
def number_account() -> str:
    return "**4305"


@pytest.mark.parametrize("number", [73654108430135874305, "73654108430135874305"])
def test_get_mask_account(number: Union[int, str], number_account: str) -> None:
    assert get_mask_account(number) == number_account


@pytest.mark.parametrize(
    "number_account", [1111222233334444555566667777, 1111222233334444, "1111222233334444aaaa", ""]
)
def test_get_mask_account_invalid(number_account: Union[int, str]) -> None:
    with pytest.raises(ValueError) as e:
        get_mask_account(1111222233334444555566667777)

    assert str(e.value) == "Номер банковского счета должен состоять из 20-ти цифровых символов"
