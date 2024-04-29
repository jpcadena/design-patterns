"""
A module for exercise in the gamma categorization.behavioral.template
 method package.
"""

from abc import ABC, abstractmethod


class Creature:
    """
    Creature class representation
    """

    def __init__(self, attack: int, health: int):
        self.initial_health: int = health  # For temporary damage reset
        self.health: int = health
        self.attack: int = attack


class CardGame(ABC):
    """
    Card Game representation from Abstract Base Class
    """

    def __init__(self, creatures: list[Creature]):
        self.creatures: list[Creature] = creatures

    def combat(self, c1_index: int, c2_index: int) -> int:
        """
        Combat in the card game
        :param c1_index: The index of the first creature
        :type c1_index: int
        :param c2_index: The index of the second creature
        :type c2_index: int
        :return: The index of the living survivor creature;
         -1 if both are alive
        :rtype: int
        """
        first: Creature = self.creatures[c1_index]
        second: Creature = self.creatures[c2_index]
        self.hit(first, second)
        self.hit(second, first)
        is_first_alive = first.health > 0
        is_second_alive = second.health > 0
        # Reset health for temporary damage games
        self.reset_health(first)
        self.reset_health(second)
        if is_first_alive == is_second_alive:
            return -1
        return c1_index if is_first_alive else c2_index

    @abstractmethod
    def hit(self, attacker: Creature, defender: Creature) -> None:
        """
        Hit abstract method for the creatures
        :param attacker: The creature that attacks
        :type attacker: Creature
        :param defender: The creature that defense
        :type defender: Creature
        :return: None
        :rtype: NoneType
        """
        pass

    @abstractmethod
    def reset_health(self, creature: Creature) -> None:
        """
        Reset health abstract method for a creature
        :param creature: The creature that will be reset the health
        :type creature: Creature
        :return: None
        :rtype: NoneType
        """
        pass


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature) -> None:
        defender.health -= attacker.attack

    def reset_health(self, creature: Creature) -> None:
        creature.health = creature.initial_health


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature) -> None:
        defender.health -= attacker.attack

    def reset_health(self, creature: Creature) -> None:
        pass  # No need to reset health in permanent damage game


# Example usage
if __name__ == "__main__":
    creature1: Creature = Creature(1, 2)
    creature2: Creature = Creature(1, 2)
    game: CardGame = TemporaryDamageCardGame([creature1, creature2])
    print(
        game.combat(0, 1)
    )  # Output will be -1 because both creatures will be alive
    creature1 = Creature(1, 1)
    creature2 = Creature(2, 2)
    game = PermanentDamageCardGame([creature1, creature2])
    print(
        game.combat(0, 1)
    )  # Output will be 1 because the second creature wins
