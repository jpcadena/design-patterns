"""
Singleton Decorator script
"""
from functools import wraps
from typing import Any


def singleton(cls: type) -> type:
    """
    Singleton function as for decorator
    :param cls: Object class instance
    :type cls: type
    :return: Wrapped class instance
    :rtype: type
    """
    instances: dict = {}

    @wraps(cls)
    def get_instance(
            *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> callable:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    cls.get_instance = get_instance
    return cls


@singleton
class Database:
    """
    Database class
    """

    def __new__(cls):
        print('Loading database')
        return super(Database, cls).__new__(cls)


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
