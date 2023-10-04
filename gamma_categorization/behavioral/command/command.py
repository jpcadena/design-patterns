"""
Command script
"""
from abc import ABC
from enum import Enum
from typing import Optional


class BankAccount:
    """
    Bank account class.
    """

    OVERDRAFT_LIMIT: int = -500

    def __init__(self, balance: int = 0):
        self.balance: int = balance

    def deposit(self, amount: int) -> None:
        """
        Deposit amount into the account
        :param amount: The amount to deposit
        :type amount: int
        :return: None
        :rtype: NoneType
        """
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount: int) -> bool:
        """
        Withdraw an amount from the account
        :param amount: The amount to withdraw
        :type amount: int
        :return: True if the amount was successfully withdraw; False
         otherwise
        :rtype: bool
        """
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, balance = {self.balance}")
            return True
        return False

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


class Command(ABC):
    """
    Command class that inherits from Abstract Base Class.
    """

    def __init__(self) -> None:
        self.success: Optional[bool] = False

    def invoke(self) -> None:
        """
        Invoke method
        :return: None
        :rtype: NoneType
        """

    def undo(self) -> None:
        """
        Undo method
        :return: None
        :rtype: NoneType
        """


class BankAccountCommand(Command):
    """
    Bank Account Command class that inherits from Command.
    """

    def __init__(self, account: BankAccount, action: Enum, amount: int):
        super().__init__()
        self.amount: int = amount
        self.action: Enum = action
        self.account: BankAccount = account
        self.success: Optional[bool] = None

    class Action(int, Enum):
        """
        Action class that inherits from Python built-in Enum.
        """

        DEPOSIT: int = 0
        WITHDRAW: int = 1

    def invoke(self) -> None:
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self) -> None:
        if not self.success:
            return
        # strictly speaking this is not correct
        # (you don't undo a deposit by withdrawing)
        # but it works for this demo, so...
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    bank_account: BankAccount = BankAccount()
    bank_account_command: BankAccountCommand = BankAccountCommand(
        bank_account, BankAccountCommand.Action.DEPOSIT, 100
    )
    bank_account_command.invoke()
    print("After $100 deposit:", bank_account)

    bank_account_command.undo()
    print("$100 deposit undone:", bank_account)

    illegal_cmd: BankAccountCommand = BankAccountCommand(
        bank_account, BankAccountCommand.Action.WITHDRAW, 1000
    )
    illegal_cmd.invoke()
    print("After impossible withdrawal:", bank_account)
    illegal_cmd.undo()
    print("After undo:", bank_account)
