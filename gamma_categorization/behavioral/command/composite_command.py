"""
Composite Command a.k.a. Macro script
"""
from typing import Any

from command import BankAccountCommand, Command

from gamma_categorization.behavioral.command.command import BankAccount


class CompositeBankAccountCommand(Command, list[Any]):  # type: ignore
    """
    Composite Bank Account Command class that inherits from Command and
     Python built-in list.
    """

    def __init__(self, items: list[Any]):
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self) -> None:
        for command in self:
            command.invoke()

    def undo(self) -> None:
        for command in reversed(self):
            command.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    """
    Money Transfer Command that inherits from Composite Bank Account
     Command.
    """

    def __init__(
        self, from_acct: BankAccount, to_acct: BankAccount, amount: int
    ):
        super().__init__(
            [
                BankAccountCommand(
                    from_acct, BankAccountCommand.Action.WITHDRAW, amount
                ),
                BankAccountCommand(
                    to_acct, BankAccountCommand.Action.DEPOSIT, amount
                ),
            ]
        )

    def invoke(self) -> None:
        invoked: bool = True
        for command in self:
            if invoked:
                command.invoke()
                invoked = command.success
            else:
                command.success = False
        self.success = invoked


if __name__ == "__main__":
    # composite deposit
    bank_account: BankAccount = BankAccount()
    AMOUNT: int = 1000
    deposit1: BankAccountCommand = BankAccountCommand(
        bank_account, BankAccountCommand.Action.DEPOSIT, AMOUNT
    )
    deposit2: BankAccountCommand = BankAccountCommand(
        bank_account, BankAccountCommand.Action.DEPOSIT, AMOUNT
    )
    composite: CompositeBankAccountCommand = CompositeBankAccountCommand(
        [deposit1, deposit2]
    )
    composite.invoke()
    print(bank_account)
    composite.undo()
    print(bank_account)

    # transfer fail
    bank_account1: BankAccount = BankAccount(100)
    bank_account2: BankAccount = BankAccount()
    withdraw = BankAccountCommand(
        bank_account1, BankAccountCommand.Action.WITHDRAW, AMOUNT
    )
    deposit = BankAccountCommand(
        bank_account2, BankAccountCommand.Action.DEPOSIT, AMOUNT
    )
    composite_bank_account_command = CompositeBankAccountCommand(
        [withdraw, deposit]
    )
    composite_bank_account_command.invoke()
    print("bank_account1:", bank_account1, "bank_account2:", bank_account2)
    composite_bank_account_command.undo()
    print("bank_account1:", bank_account1, "bank_account2:", bank_account2)

    # better transfer
    money_transfer_command: MoneyTransferCommand = MoneyTransferCommand(
        bank_account1, bank_account2, AMOUNT
    )
    money_transfer_command.invoke()
    print("bank_account1:", bank_account1, "bank_account2:", bank_account2)
    money_transfer_command.undo()
    print("bank_account1:", bank_account1, "bank_account2:", bank_account2)
    print(money_transfer_command.success)
