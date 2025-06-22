from src.process_bank import process_bank_operations, process_bank_search


def test_process_bank_search(transactions: list[dict]) -> None:
    result = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    assert process_bank_search(transactions, "на карту")[0] == result


def test_process_bank_operations(transactions: list[dict]) -> None:
    result = {"Перевод с карты на карту": 1}
    assert process_bank_operations(transactions, ["Перевод с карты на карту"]) == result
