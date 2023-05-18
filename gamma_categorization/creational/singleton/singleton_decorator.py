"""
Singleton Decorator script
"""
from functools import wraps
from typing import Any, Type


def singleton(cls: Type[Any]) -> Type[Any]:
    """
    Singleton function as for decorator
    :param cls: Object class instance
    :type cls: type
    :return: Wrapped class instance
    :rtype: type
    """
    instances: dict[Any, Any] = {}

    @wraps(cls)
    def get_instance(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
        """
        Get instance of Singleton class
        :param args: The arguments
        :type args: tuple[Any, ...]
        :param kwargs: The keyword arguments
        :type kwargs: dict[str, Any]
        :return: The instance of singleton class
        :rtype: Any
        """
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
        print("Loading database")
        return super(Database, cls).__new__(cls)


if __name__ == "__main__":
    d1: Database = Database()
    d2: Database = Database()
    print(d1 == d2)
