from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import get_transaction_amount


@patch("requests.get")
def test_get_transaction_amount(mock_request: Any) -> None:
    mock_request.return_value.json.return_value = {"result": 100.0}

    assert (
        get_transaction_amount(
            {
                "id": 854048120,
                "state": "EXECUTED",
                "date": "2019-03-29T10:57:20.635567",
                "operationAmount": {"amount": "30234.99", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на счет",
                "from": "Visa Classic 1203921041964079",
                "to": "Счет 34616199494072692721",
            }
        )
        == 100.0
    )


@pytest.mark.parametrize("values", [{}, []])
def test_get_transaction_amount_1(values: Any) -> None:
    with pytest.raises(ValueError) as e:
        get_transaction_amount(values)
    assert str(e.value) == "Некорректный формат транзакции"


def test_get_transaction_amount_2() -> None:
    assert (
        get_transaction_amount(
            {
                "id": 894961746,
                "state": "EXECUTED",
                "date": "2019-08-04T20:17:25.443322",
                "operationAmount": {"amount": "2523.44", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 33721541831646393763",
                "to": "Счет 68774571780974952778",
            }
        )
        == 2523.44
    )


def test_get_transaction_amount_3() -> None:
    with pytest.raises(ValueError) as e:
        get_transaction_amount(
            {
                "id": 894961746,
                "state": "EXECUTED",
                "date": "2019-08-04T20:17:25.443322",
                "operationAmount": {
                    "amount": "2523.44",
                    "currency": {
                        "name": "руб.",
                    },
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 33721541831646393763",
                "to": "Счет 68774571780974952778",
            }
        )

    assert str(e.value) == "Некорректный формат транзакции"
