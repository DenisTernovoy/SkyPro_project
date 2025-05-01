from typing import Any, Callable


def log(filename: str = "") -> Callable:
    def wrapper(function: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> None:
            name = function.__name__
            try:
                response = function(*args, **kwargs)
                result = f"{name} {response}"
            except Exception as e:
                result = f"{name} error: {e}. Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, "w") as file:
                    file.write(result)
            else:
                print(result)

        return inner

    return wrapper
