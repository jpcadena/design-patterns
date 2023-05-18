"""
Chain of Responsibility Coding Exercise
"""


class Creature:
    """
    Creature class
    """

    def __init__(self, game) -> None:
        self.game: Game = game


class Goblin(Creature):
    """
    Goblin class that inherits from Creature
    """

    def __init__(self, game) -> None:
        super().__init__(game)
        game.creatures.append(self)

    @property
    def attack(self) -> int:
        """
        The getter method for attack attribute.
        :return: The attack
        :rtype: int
        """
        attack: int = 1
        for creature in self.game.creatures:
            if isinstance(creature, GoblinKing):
                attack += 1
        return attack

    @property
    def defense(self) -> int:
        """
        The getter method for defense attribute.
        :return: The defense
        :rtype: int
        """
        defense: int = 1
        num_goblins: int = (
                sum(
                    isinstance(creature, Goblin)
                    for creature in self.game.creatures
                )
                - 1
        )
        defense += num_goblins
        return defense


class GoblinKing(Goblin):
    """
    Goblin class that inherits from Goblin
    """

    @property
    def attack(self) -> int:
        return 3

    @property
    def defense(self) -> int:
        return 3


class Game:
    """
    Game class.
    """

    def __init__(self) -> None:
        self.creatures: list[Creature] = []
