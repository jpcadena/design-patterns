"""
A module for intrusive in the gamma categorization.behavioral.visitor package.
"""

from typing import Self, Union


class DoubleExpression:
    """
    Double expression class
    """

    def __init__(self, value: int):
        self.value: int = value

    def print(self, buffer: list[str]) -> None:
        """
        Prints the double expression
        :param buffer: The buffer that represents the double expression
        :type buffer: list[str]
        :return: None
        :rtype: NoneType
        """
        buffer.append(str(self.value))

    def eval(self) -> int:
        """
        Evaluates the double expression
        :return: The value of the double expression
        :rtype: int
        """
        return self.value


class AdditionExpression:
    """
    Addition expression class
    """

    def __init__(
        self,
        left: Union[DoubleExpression, Self],
        right: Union[DoubleExpression, Self],
    ):
        self.right: Union[DoubleExpression, Self] = right
        self.left: Union[DoubleExpression, Self] = left

    def print(self, buffer: list[str]) -> None:
        """
        Prints the addition expression
        :param buffer: The buffer that represents the addition expression
        :type buffer: list[str]
        :return: None
        :rtype: NoneType
        """
        buffer.append("(")
        self.left.print(buffer)
        buffer.append("+")
        self.right.print(buffer)
        buffer.append(")")

    def eval(self) -> int:
        """
        Evaluate the addition expression
        :return: The result from addition
        :rtype: int
        """
        return self.left.eval() + self.right.eval()


if __name__ == "__main__":
    # represents 1+(2+3)
    e: AdditionExpression = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )
    my_buffer: list[str] = []
    e.print(my_buffer)
    print("".join(my_buffer), "=", e.eval())

    # breaks OCP: requires we modify the entire hierarchy
    # what is more likely: new type or new operation?
