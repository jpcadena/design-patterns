"""
A module for visitor refined in the gamma categorization.behavioral.visitor
 package.
"""

from typing import Optional

from gamma_categorization.behavioral.visitor.visitor import (
    AdditionExpression,
    DoubleExpression,
    ExpressionPrinter,
    visitor,
)


class ExpressionEvaluator:
    """A class for evaluating expressions."""

    def __init__(self) -> None:
        self.value: Optional[int] = None

    @visitor(DoubleExpression)
    def visit_double_expression(self, de: DoubleExpression) -> None:
        """
        Visit a DoubleExpression.
        :param de: The DoubleExpression to visit.
        :return: None
        """
        self.value = de.value

    @visitor(AdditionExpression)
    def visit_addition_expression(self, ae: AdditionExpression) -> None:
        """
        Visit an AdditionExpression.
        :param ae: The AdditionExpression to visit.
        :return: None
        """
        self.visit_addition_expression(ae.left)  # Recursively visit left
        temp: Optional[int] = self.value
        self.visit_addition_expression(ae.right)  # Recursively visit right

        if temp is not None and self.value is not None:
            self.value += temp


if __name__ == "__main__":
    # represents 1+(2+3)
    e: AdditionExpression = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )
    printer: ExpressionPrinter = ExpressionPrinter()
    # Call the appropriate methods
    printer.visit_double_expression(e.left)
    printer.visit_addition_expression(e.right)
    evaluator: ExpressionEvaluator = ExpressionEvaluator()
    # Call the appropriate methods
    evaluator.visit_double_expression(e.left)
    evaluator.visit_addition_expression(e.right)
    if evaluator.value is not None:
        print(f"{printer} = {evaluator.value}")
