"""
A module for memento in the gamma categorization.behavioral.memento package.
"""


class Memento:
    """
    Memento class for representation of current state
    """

    def __init__(self, balance: int):
        self.balance: int = balance


class BankAccount:
    """
    A class to represent a bank account
    """

    def __init__(self, balance: int = 0):
        self.balance: int = balance

    def deposit(self, amount: int) -> Memento:
        """
        Deposit command for a bank account
        :param amount: The amount to deposit
        :type amount: int
        :return: The current state of bank account
        :rtype: Memento
        """
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento: Memento) -> None:
        """
        Restore command for a bank account
        :param memento: The state to roll back
        :type memento: Memento
        :return: None
        :rtype: NoneType
        """
        self.balance = memento.balance

    def __str__(self) -> str:
        return f'Balance = {self.balance}'


if __name__ == '__main__':
    bank_account: BankAccount = BankAccount(100)
    memento1: Memento = bank_account.deposit(50)
    memento2: Memento = bank_account.deposit(25)
    print(bank_account)
    # restore to memento1
    bank_account.restore(memento1)
    print(bank_account)
    # restore to memento2
    bank_account.restore(memento2)
    print(bank_account)
