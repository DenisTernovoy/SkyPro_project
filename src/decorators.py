from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Декоратор с параметрами, записывающий результат работы передаваемой ему функции в консоль или файл 'filename'
    и возвращающий результат работы этой функции"""

    def wrapper(function: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any:
            name = function.__name__

            try:
                result_func = function(*args, **kwargs)
                result = f"{name} {result_func}"
            except Exception as e:
                result_func = None
                result = f"{name} error: {e}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, "w") as file:
                    file.write(result)
            else:
                print(result)

            return result_func

        return inner

    return wrapper


@log()
def my_func(x: int, y: int) -> float:
    return x / y


print(my_func(2, 0))
