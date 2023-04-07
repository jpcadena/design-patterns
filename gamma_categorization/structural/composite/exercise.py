"""
Composite Coding Exercise
"""
from typing import Union


class Summable:
    """
    Summable class that provides the sum property.
    """

    def __iter__(self):
        raise NotImplementedError

    @property
    def sum(self) -> int:
        """
        Sum property
        :return: Result value from sum operation
        :rtype: int
        """
        result: int = 0
        for item in self:
            if isinstance(item, (int, SingleValue)):
                result += item
            elif isinstance(item, ManyValues):
                result += item.sum
        return result


class SingleValue(Summable):
    """
    Single Value class that inherits from Summable
    """

    def __init__(self, value: int):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, Summable):
    """
    Many Values class that inherits from list and Summable
    """

    def append(self, value: Union[int, SingleValue, 'ManyValues']) -> None:
        """
        Overwrite for append method from lists
        :param value: The value to append
        :type value: Union[int, SingleValue, 'ManyValues']
        :return: None
        :rtype: NoneType
        """
        super().append(value)
