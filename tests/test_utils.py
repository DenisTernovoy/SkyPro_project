import os
from typing import Any
from unittest.mock import mock_open, patch

from src.utils import get_transactions_info

from pathlib import Path

#  Путь до корневой директории
BASE_DIR = Path(__file__).resolve().parent.parent
OPERATIONS_PATH = BASE_DIR.joinpath('data', 'operations.json')

file_path = str(OPERATIONS_PATH).replace('\\', '/')

def test_get_transactions_info_1() -> None:
    mock_data = [{"key": "value"}, {"key": "value"}]

    with patch("src.utils.json.load", return_value=mock_data):
        result = get_transactions_info(file_path)

    assert result == mock_data


def test_get_transactions_info_2() -> None:
    mock_data = ""

    with patch("json.load", return_value=mock_data):
        result = get_transactions_info(file_path)

    assert result == []


@patch("os.path.isfile", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="{'key': 'value')")
def test_get_transactions_info_3(mock_open: Any, mock_isfile: Any) -> None:
    file = "test_file.json"
    result = get_transactions_info(file)
    assert result == []


def test_get_transactions_info_invalid_path() -> None:
    assert get_transactions_info("") == []
