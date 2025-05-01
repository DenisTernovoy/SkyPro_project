from typing import Any, Callable


def log(filename: str = "") -> Callable:
    def wrapper(function: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any:
            name = function.__name__
            try:
                result = f"{name} {function(*args, **kwargs)}"
            except Exception as e:
                result = f"{name} error: {e}. Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, "w") as file:
                    file.write(result)
            else:
                print(result)
            return function(*args, **kwargs)

        return inner

    return wrapper
