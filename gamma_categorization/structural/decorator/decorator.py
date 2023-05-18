"""
Python functional Decorator script
"""
import time
from typing import Any, Callable


def time_it(func: Callable[[], Any]) -> Any:
    """
    Decorator function that calculates the time that the function takes
     to execute
    :param func: The function to be called
    :type func: Callable
    :return: Return value from the wrapped function
    :rtype: Any
    """

    def wrapper() -> Any:
        """
        The wrapper function
        :return: The result of the wrapped function
        :rtype: Any
        """
        start: float = time.time()
        result: Any = func()
        end: float = time.time()
        print(f"{func.__name__}: took {int(end - start)} seconds")
        return result

    return wrapper


@time_it
def some_op() -> int:
    """
    Some function to execute an operation
    :return: Some value
    :rtype: int
    """
    print("Starting op")
    time.sleep(1)
    print("Finished op")
    return 123


if __name__ == "__main__":
    # some_op()
    # time_it(some_op)()
    some_op()
