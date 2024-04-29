"""
A module for exercise in the gamma categorization.behavioral.interpreter
 package.
"""


class ExpressionProcessor:
    """
    The processor class for the expression
    """

    def __init__(self) -> None:
        self.variables: dict[str, int] = {}

    def calculate(self, expression: str) -> int:
        """
        Calculate the expression operation
        :param expression: The expression to calculate
        :type expression: str
        :return: The expression result
        :rtype: int
        """
        # initialize result to 0
        total: int = 0
        current_number: str = ""  # to keep track of current number/variable
        operation: int = 1  # 1 for addition, -1 for subtraction
        # append '+' to process the last number/variable in the loop
        expression += "+"
        for char in expression:
            if char in ["+", "-"]:
                # check if current_number is a digit
                if current_number.isdigit():
                    total += operation * int(current_number)
                elif len(current_number) == 1:  # single-letter variable
                    # check if variable exists
                    if current_number in self.variables:
                        total += operation * self.variables[current_number]
                    else:  # variable not found
                        return 0
                else:  # parsing failure or multi-letter variable
                    return 0
                # reset current_number for the next number/variable
                current_number = ""
                # set the next operation
                operation = 1 if char == "+" else -1
            else:
                current_number += char
        return total
