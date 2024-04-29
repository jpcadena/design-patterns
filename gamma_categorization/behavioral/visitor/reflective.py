"""
A module for reflective in the gamma categorization.behavioral.visitor package.
"""

from abc import ABC


class Expression(ABC):
    """
    Abstract Base Class for Expression
    """

    pass


class DoubleExpression(Expression):
    def __init__(self, value: int):
        self.value: int = value


class AdditionExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.right: Expression = right
        self.left: Expression = left


class ExpressionPrinter:
    """
    The expression printer interface
    """

    @staticmethod
    def print(expression: Expression, buffer: list[str]) -> None:
        """Will fail silently on a missing case."""
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(")")

    Expression.print = lambda self, b: ExpressionPrinter.print(  # type: ignore
        self, b
    )


# still breaks OCP because new types require M×N modifications

if __name__ == "__main__":
    # represents 1+(2+3)
    additional_expression: AdditionExpression = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )
    my_buffer: list[str] = []

    ExpressionPrinter.print(additional_expression, my_buffer)
    # IDE might complain here
    # additional_expression.print(my_buffer)

    print("".join(my_buffer))
