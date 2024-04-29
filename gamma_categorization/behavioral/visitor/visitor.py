"""
A module for visitor in the gamma categorization.behavioral.visitor package.
"""

from typing import Any, Callable, Type, Union

_methods: dict[tuple[str, Type[Any]], Callable[[Any, Any], None]] = {}


def _qualname(obj: Any) -> str:
    """
    Get the fully-qualified name of an object (including module).
    :param obj: The object to get the fully-qualified name
    :type obj: Any
    :return: The fully-qualified name of the object
    :rtype: str
    """
    return str(obj.__module__ + "." + obj.__qualname__)


def _declaring_class(obj: Any) -> str:
    """
    Get the name of the class that declared an object.
    :param obj: The object to get the name of
    :type obj: Any
    :return: The filtered name
    :rtype: str
    """
    name: str = _qualname(obj)
    return name[: name.rfind(".")]


def _visitor_impl(self: Any, arg: Any) -> None:
    """
    Actual visitor method implementation.
    :param self: The visitor object.
    :type self: Any
    :param arg: The object to be visited.
    :type arg: Any
    :return: None
    :rtype: NoneType
    """
    method = _methods[(_qualname(type(self)), type(arg))]
    method(self, arg)


def visitor(
    arg_type: Type[Any],
) -> Callable[[Callable[[Any, Any], None]], Callable[[Any, Any], None]]:
    """
    Decorator that creates a visitor method.

    :param arg_type: The type of the argument that the method should accept.
    :return: A decorator that transforms a method into a visitor method.
    """

    def decorator(fn: Callable[[Any, Any], None]) -> Callable[[Any, Any], None]:
        """
        Decorator that creates a visitor method
        :param fn: The function to execute the visitor method
        :type fn: Callable[[Any, Any], None]
        :return: The visitor method
        :rtype: Callable[[Any, Any], None]
        """
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn
        return _visitor_impl

    return decorator


class DoubleExpression:
    """
    Double Expression representation class
    """

    def __init__(self, value: int):
        self.value: int = value

    def accept(self, visitor: Any) -> None:
        """
        Accept a visitor.
        :param visitor: The visitor to accept
        :type visitor: Any
        :return: None
        :rtype: NoneType
        """
        visitor.visit(self)


class AdditionExpression:
    """
    Addition of an expression
    """

    def __init__(
        self,
        left: Union["AdditionExpression", DoubleExpression],
        right: Union["AdditionExpression", DoubleExpression],
    ):
        """
        Initialize an AdditionExpression.

        :param left: The left expression.
        :param right: The right expression.
        """
        self.left: Union["AdditionExpression", DoubleExpression] = left
        self.right: Union["AdditionExpression", DoubleExpression] = right

    def accept(self, visitor: Any) -> None:
        """Accept a visitor."""
        visitor.visit(self)


class ExpressionPrinter:
    """
    Expression Printer class
    """

    def __init__(self) -> None:
        """Initialize an ExpressionPrinter."""
        self.buffer: list[str] = []

    @visitor(DoubleExpression)
    def visit_double_expression(self, de: DoubleExpression) -> None:
        """Visit a DoubleExpression."""
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit_addition_expression(self, ae: AdditionExpression) -> None:
        """Visit an AdditionExpression."""
        self.buffer.append("(")
        ae.left.accept(self)
        self.buffer.append("+")
        ae.right.accept(self)
        self.buffer.append(")")

    def __str__(self) -> str:
        """Convert the buffer to a string."""
        return "".join(self.buffer)


if __name__ == "__main__":
    # represents 1+(2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )
    printer: ExpressionPrinter = ExpressionPrinter()
    printer.visit(e)  # type: ignore
    print(printer)
