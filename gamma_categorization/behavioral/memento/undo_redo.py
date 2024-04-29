"""
A module for undo redo in the gamma categorization.behavioral.memento package.
"""

from typing import Optional

from gamma_categorization.behavioral.memento.memento import Memento


class BankAccount:
    """
    A class to represent a bank account
    """

    def __init__(self, balance: int = 0):
        self.balance: int = balance
        self.changes: list[Memento] = [Memento(self.balance)]
        self.current: int = 0

    def deposit(self, amount: int) -> Memento:
        """
        Deposit command for a bank account
        :param amount: The amount to deposit
        :type amount: int
        :return: The current state of bank account
        :rtype: Memento
        """
        self.balance += amount
        memento: Memento = Memento(self.balance)
        self.changes.append(memento)
        self.current += 1
        return memento

    def restore(self, memento: Memento) -> None:
        """
        Restore command for a bank account
        :param memento: The state to roll back
        :type memento: Memento
        :return: None
        :rtype: NoneType
        """
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes) - 1

    def undo(self) -> Optional[Memento]:
        """
        Undo command for the bank account
        :return: The previous state of bank account
        :rtype: Optional[Memento]
        """
        if self.current > 0:
            self.current -= 1
            memento: Memento = self.changes[self.current]
            self.balance = memento.balance
            return memento
        return None

    def redo(self) -> Optional[Memento]:
        """
        Redo command for the bank account
        :return: The next state of bank account that was undone
        :rtype: Optional[Memento]
        """
        if self.current + 1 < len(self.changes):
            self.current += 1
            memento: Memento = self.changes[self.current]
            self.balance = memento.balance
            return memento
        return None

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    bank_account: BankAccount = BankAccount(100)
    bank_account.deposit(50)
    bank_account.deposit(25)
    print(bank_account)
    bank_account.undo()
    print(f"Undo 1: {bank_account}")
    bank_account.undo()
    print(f"Undo 2: {bank_account}")
    bank_account.redo()
    print(f"Redo 1: {bank_account}")
