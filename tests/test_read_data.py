from typing import Any
from unittest.mock import Mock, patch

import pandas

from src.read_data import read_csv_file, read_excel_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_data: Any) -> None:
    mock_data.return_value.to_dict.return_value = [{}, {}]
    assert read_csv_file("") == [{}, {}]


def test_read_csv_file_invalid(capsys: Any) -> None:
    mock_data = Mock(side_effect=Exception("Ошибка"))
    pandas.read_csv = mock_data
    read_csv_file("")
    captured = capsys.readouterr()
    assert captured.out == "Произошла ошибка при попытке считать файл: Ошибка\n"


@patch("pandas.read_excel")
def test_read_excel_file(mock_data: Any) -> None:
    mock_data.return_value.to_dict.return_value = [{}, {}]
    assert read_excel_file("") == [{}, {}]


def test_read_excel_file_invalid(capsys: Any) -> None:
    mock_data = Mock(side_effect=Exception("Ошибка"))
    pandas.read_excel = mock_data
    read_excel_file("")
    captured = capsys.readouterr()
    assert captured.out == "Произошла ошибка при попытке считать файл: Ошибка\n"
