"""
A module for exercise in the gamma categorization.behavioral.visitor package.
"""

from typing import Any, Callable, Type, Union


def _qualname(obj: Any) -> str:
    """
    Get the fully-qualified name of an object (including module).
    :param obj: The object to get the fully-qualified name
    :type obj: object
    :return: Fully-qualified name
    :rtype: str
    """
    return str(obj.__module__ + "." + obj.__qualname__)


def _declaring_class(obj: object) -> str:
    """
    Get the name of the class that declared an object.
    :param obj: The object to get the name of
    :type obj: object
    :return: Name of declaring class
    :rtype: str
    """
    name: str = _qualname(obj)
    return name[: name.rfind(".")]


_methods: dict[tuple[str, Type[Any]], Callable[[Any, Any], None]] = {}


def _visitor_impl(self: object, arg: object) -> None:
    """
    Actual visitor method implementation.
    :param self: The visitor object to get the method from
    :type self: object
    :param arg: The object to be visited
    :type arg: object
    :return: None
    :rtype: NoneType
    """
    method = _methods[(_qualname(type(self)), type(arg))]
    method(self, arg)


def visitor(
    arg_type: type,
) -> Callable[[Callable[[Any, Any], None]], Callable[[Any, Any], None]]:
    """
    Decorator that creates a visitor method.
    :param arg_type: The type of argument that the method should accept
    :type arg_type: type
    :return: Decorator
    :rtype: callable
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


# Existing code ends


class Value:
    """
    The value class representation
    """

    def __init__(self, value: int) -> None:
        self.value: int = value


class AdditionExpression:
    """
    The addition expression
    """

    def __init__(self, left: "Expression", right: "Expression") -> None:
        self.right: "Expression" = right
        self.left: "Expression" = left


class MultiplicationExpression:
    """
    The multiplication expression
    """

    def __init__(self, left: "Expression", right: "Expression") -> None:
        self.right: "Expression" = right
        self.left: "Expression" = left


Expression = Union[Value, AdditionExpression, MultiplicationExpression]


class ExpressionPrinter:
    """
    The printer expression class representation
    """

    def __init__(self) -> None:
        self.buffer: list[str] = []

    @visitor(Value)
    def visit(self, value: Value) -> None:
        """
        Visit a Value expression.
        :param value: The Value expression
        :type value: Value
        :return: None
        :rtype: NoneType
        """
        self.buffer.append(str(value.value))

    @visitor(AdditionExpression)  # type: ignore
    def visit(self, ae: AdditionExpression) -> None:  # noqa: F811
        """
        Visit an AdditionExpression.
        :param ae: The Addition Expression
        :type ae: AdditionExpression
        :return: None
        :rtype: NoneType
        """
        self.buffer.append("(")
        self.visit(ae.left)
        self.buffer.append("+")
        self.visit(ae.right)
        self.buffer.append(")")

    @visitor(MultiplicationExpression)  # type: ignore
    def visit(self, me: MultiplicationExpression) -> None:  # noqa: F811
        """
        Visit a MultiplicationExpression.
        :param me: The Multiplication Expression
        :type me: MultiplicationExpression
        :return: None
        :rtype: NoneType
        """
        self.visit(me.left)
        self.buffer.append("*")
        self.visit(me.right)

    def __str__(self) -> str:
        """
        Convert the buffer to a string.
        :return: String representation
        :rtype: str
        """
        return "".join(self.buffer)
