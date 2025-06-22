from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:

        def write_log(message: str, filename: Optional[str] = None) -> None:
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(message)
            else:
                print(message)

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} - OK - {result}\n"
                write_log(message, filename)
                return result
            except Exception as e:
                message = f"{func.__name__} - {type(e)} - args: {args} - kwargs: {kwargs}\n"
                write_log(message, filename)
                raise

        return wrapper

    return decorator
