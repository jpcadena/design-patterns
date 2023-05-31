"""
Singleton Metaclass script
"""
from typing import Any


class Singleton(type):
    """
    Metaclass that creates a Singleton base type when called.
    """

    _instances: dict[Any, Any] = {}

    def __call__(cls, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class Database(metaclass=Singleton):
    """
    Database class that uses a metaclass based on Singleton
    """

    def __init__(self) -> None:
        print("Loading database")


if __name__ == "__main__":
    d1: Database = Database()
    d2: Database = Database()
    print(d1 == d2)
