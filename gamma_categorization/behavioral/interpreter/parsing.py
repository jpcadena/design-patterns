"""
A module for parsing in the gamma categorization.behavioral.interpreter package.
"""
from enum import Enum
from typing import Optional

from gamma_categorization.behavioral.interpreter.lexing import (
    Expression,
    Token,
    lex,
)


class Integer(Expression):
    """
    Integer representation
    """

    def __init__(self, value: int):
        self._value: int = value

    @property
    def value(self) -> int:
        return self._value


class BinaryOperation(Expression):
    """
    A binary operation representation
    """

    class Type(Enum):
        """
        The type of operation representation
        """

        ADDITION: int = 0
        SUBTRACTION: int = 1

    def __init__(self) -> None:
        self.type: Optional[Enum] = None
        self.left: Optional[Expression] = None
        self.right: Optional[Expression] = None

    @property
    def value(self) -> int:
        """
        The value of the operation
        :return: The integer value from operation
        :rtype: int
        """
        if not self.left or not self.right:  # Handle None values
            raise ValueError("Left or Right operand missing")
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        return self.left.value - self.right.value


def parse(tokens: list[Token]) -> BinaryOperation:
    """
    Parse a list of tokens into a binary operation
    :param tokens: The list of tokens to parse
    :type tokens: list[Token]
    :return: The result from Binary operation
    :rtype: BinaryOperation
    """
    result: BinaryOperation = BinaryOperation()
    have_lhs: bool = False
    i: int = 0
    while i < len(tokens):
        token: Token = tokens[i]
        if token.type == Token.Type.INTEGER:
            integer: Integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryOperation.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryOperation.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:  # note: no if for RPAREN
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            # preprocess subexpression
            subexpression = tokens[i + 1 : j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j  # advance
        i += 1
    return result


def evaluate(_input: str) -> None:
    """
    Evaluate the expression
    :param _input: The input string
    :type _input: str
    :return: None
    :rtype: NoneType
    """
    tokens: list[Token] = lex(_input)
    print(' '.join(map(str, tokens)))
    parsed: BinaryOperation = parse(tokens)
    print(f'{_input} = {parsed.value}')


if __name__ == '__main__':
    evaluate('(13+4)-(12+1)')
    evaluate('1+(3-4)')
    # this won't work
    evaluate('1+2+(3-4)')
