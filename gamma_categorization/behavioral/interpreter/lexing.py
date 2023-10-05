"""
A module for lexing in the gamma categorization.behavioral.interpreter package.
"""
from abc import ABC
from enum import Enum


class Expression(ABC):
    """
    A class for abstract base expression
    """

    @property
    def value(self) -> int:
        """
        The value of the expression
        :return: Not implemented
        :rtype: int
        """
        raise NotImplementedError


class Token:
    """
    Token class for lexing in an Interpreter
    """

    class Type(Enum):
        """
        Type class for lexing
        """

        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4

    def __init__(self, _type: Type, text: str):
        self.type = _type
        self.text: str = text

    def __str__(self) -> str:
        return f'`{self.text}`'


def lex(_input: str) -> list[Token]:
    """
    Lexing a string
    :param _input: The input string
    :type _input: str
    :return: The list of tokens
    :rtype: list[Token]
    """
    result: list[Token] = []
    i: int = 0
    while i < len(_input):
        if _input[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif _input[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif _input[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif _input[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:  # must be a number
            digits: list[str] = [_input[i]]
            for j in range(i + 1, len(_input)):
                if _input[j].isdigit():
                    digits.append(_input[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
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


if __name__ == '__main__':
    evaluate('(13+4)-(12+1)')
    evaluate('1+(3-4)')
    # this won't work
    evaluate('1+2+(3-4)')
