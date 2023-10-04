"""
Command Coding Exercise
"""
from enum import Enum


class Command:
    """
    Command class
    """

    class Action(Enum):
        """
        Action class based on Enum
        """

        DEPOSIT: int = 0
        WITHDRAW: int = 1

    def __init__(self, action: Action, amount: int):
        self.action = action
        self.amount: int = amount
        self.success: bool = False


class Account:
    """
    Account class for bank accounts
    """

    def __init__(self, balance: int = 0):
        self.balance: int = balance

    def process(self, command: Command) -> None:
        """
        Process command for bank account
        :param command: The command to process
        :type command: Command
        :return: None
        :rtype: NoneType
        """
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Command.Action.WITHDRAW:
            if self.balance >= command.amount:
                self.balance -= command.amount
                command.success = True
            else:
                command.success = False
