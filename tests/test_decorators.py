from typing import Any

from src.decorators import log


def test_log_1() -> None:
    @log()
    def my_func(x: int) -> int:
        return x

    a = my_func(2)
    assert a == 2


def test_log_2(capsys: Any) -> None:
    @log()
    def my_func(x: int, y: int) -> float:
        return x / y

    my_func(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_func 2.0\n"


def test_log_3(capsys: Any) -> None:
    @log()
    def my_func(x: int, y: int) -> float:
        return x / y

    my_func(2, 0)

    captured = capsys.readouterr()
    assert captured.out == "my_func error: division by zero. Inputs: (2, 0), {{}}\n"


def test_log_4() -> None:
    @log(filename="mylog.txt")
    def my_func(x: int, y: int) -> float:
        return x / y

    my_func(4, 2)

    with open("mylog.txt", "r") as file:
        text = file.read()
    assert text == "my_func 2.0"
