"""
Monostate script
"""
from typing import Any, Self


class CEO:
    """
    Chief Executive Officer class
    """

    __shared_state: dict[str, Any] = {"name": "Steve", "age": 55}

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state
        self.name: str = self.__shared_state["name"]
        self.age: int = self.__shared_state["age"]

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


class Monostate:
    """
    Monostate class
    """

    _shared_state: dict[str, Any] = {}

    def __new__(cls, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Self:
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    """
    Chief Financial Officer class
    """

    def __init__(self) -> None:
        self.name: str = ""
        self.money_managed: int = 0

    def __str__(self) -> str:
        return f"{self.name} manages ${self.money_managed}bn"


if __name__ == "__main__":
    ceo1: CEO = CEO()
    print(ceo1)

    ceo1.age = 66

    ceo2: CEO = CEO()
    ceo2.age = 77
    print(ceo1)
    print(ceo2)

    ceo2.name = "Tim"

    ceo3: CEO = CEO()
    print(ceo1, ceo2, ceo3)

    cfo1: CFO = CFO()
    cfo1.name = "Sheryl"
    cfo1.money_managed = 1

    print(cfo1)

    cfo2: CFO = CFO()
    cfo2.name = "Ruth"
    cfo2.money_managed = 10
    print(cfo1, cfo2, sep="\n")
