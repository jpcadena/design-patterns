"""
A module for exercise in the gamma categorization.behavioral.observer package.
"""

from typing import Any


class Game:
    """
    The game class
    """

    def __init__(self) -> None:
        self.rats: list["Rat"] = []
        self.rat_attack: int = 0

    def attach(self, rat: "Rat") -> None:
        """
        Attach a rat to the game
        :param rat: The rat to attach
        :type rat: Rat
        :return: None
        :rtype: NoneType
        """
        self.rats.append(rat)
        self._update_rat_attack(1)

    def detach(self, rat: "Rat") -> None:
        """
        Detach a rat from the game
        :param rat: The rat to detach
        :type rat: Rat
        :return: None
        :rtype: NoneType
        """
        self.rats.remove(rat)
        self._update_rat_attack(-1)

    def _update_rat_attack(self, change: int) -> None:
        self.rat_attack += change
        for rat in self.rats:
            rat.attack = self.rat_attack


class Rat:
    """
    The rat class representation
    """

    def __init__(self, game: Game):
        self.game: Game = game
        self.attack: int = 1
        self.game.attach(self)

    def __enter__(self) -> "Rat":
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        self.game.detach(self)
