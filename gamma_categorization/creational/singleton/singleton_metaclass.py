"""
Singleton Metaclass script
"""
from typing import Any


class Singleton(type):
    """
    Metaclass that creates a Singleton base type when called.
    """
    _instances: dict = {}

    def __call__(cls, *args: tuple[Any, ...], **kwargs: dict[str, Any]):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    """
    Database class that uses a metaclass based on Singleton
    """

    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
