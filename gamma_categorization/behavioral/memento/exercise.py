"""
A module for exercise in the gamma categorization.behavioral.memento package.
"""
from copy import deepcopy


class Token:
    """
    The token class
    """

    def __init__(self, value: int = 0):
        self.value: int = value

    def __repr__(self) -> str:
        return f'Token({self.value})'


class Memento:
    """
    Memento class for representation of current state
    """

    def __init__(self, tokens: list[Token]):
        # Use deepcopy to create a deep copy of the tokens list
        self._snapshot: list[Token] = deepcopy(tokens)

    def get_snapshot(self) -> list[Token]:
        """
        Get the current state of the tokens
        :return: The current state of the tokens
        :rtype: list[Token]
        """
        return deepcopy(self._snapshot)


class TokenMachine:
    """
    Token machine representation
    """

    def __init__(self) -> None:
        self.tokens: list[Token] = []

    def add_token_value(self, value: int) -> Memento:
        """
        Add token value
        :param value: The value to add to the machine
        :type value: int
        :return: The current state of the machine
        :rtype: Memento
        """
        return self.add_token(Token(value))

    def add_token(self, token: Token) -> Memento:
        """
        Add token to the machine
        :param token: The token itself
        :type token: Token
        :return: The current state of the machine
        :rtype: Memento
        """
        self.tokens.append(token)
        # Create a memento and return
        return Memento(self.tokens)

    def revert(self, memento: Memento) -> None:
        """
        Revert the current state of the machine
        :param memento: The state to revert
        :type memento: Memento
        :return: None
        :rtype: NoneType
        """
        self.tokens = memento.get_snapshot()
