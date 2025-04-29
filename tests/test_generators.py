import pytest

from generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency() -> None:
    result = list(
        filter_by_currency(
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            "USD",
        )
    )
    assert result == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


@pytest.mark.parametrize(
    "list_data",
    [
        [""],
        [{}, {}],
        [
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            }
        ],
    ],
)
def test_filter_by_currency_invalid(list_data: list[dict]) -> None:
    result = list(filter_by_currency(list_data, currency="EUR"))
    assert result == []


def test_transaction_descriptions(transactions: list[dict]) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize("transact", [[], [{}, {}], [""]])
def test_transaction_descriptions_invalid(transact: list[dict]) -> None:
    result = list(transaction_descriptions(transact))
    assert result == []


def test_card_number_generator(range_number: tuple[int, int]) -> None:
    result = list(card_number_generator(range_number[0], range_number[1]))
    assert result == [
        "0000 0000 0000 1000",
        "0000 0000 0000 1001",
        "0000 0000 0000 1002",
        "0000 0000 0000 1003",
        "0000 0000 0000 1004",
        "0000 0000 0000 1005",
        "0000 0000 0000 1006",
        "0000 0000 0000 1007",
        "0000 0000 0000 1008",
        "0000 0000 0000 1009",
        "0000 0000 0000 1010",
    ]
