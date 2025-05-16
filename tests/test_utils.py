import json
import os
from unittest.mock import patch, MagicMock, mock_open

import pytest

from src.utils import get_transactions_info


if os.getcwd() == 'C:\\Users\\denis\\Desktop\\BankWidget\\tests':
    file_path = '../data/operations.json'
else:
    file_path = './data/operations.json'


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


@patch('os.path.isfile', return_value=True)
@patch('builtins.open', new_callable=mock_open, read_data="{'key': 'value')")
def test_get_transactions_info_3(mock_open, mock_isfile):
    file = "test_file.json"
    result = get_transactions_info(file)
    assert result == []


def test_get_transactions_info_invalid_path() -> None:
    assert get_transactions_info("") == []
