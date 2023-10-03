"""
Broker chain script.
Build an event broker (construct of observer)
Event: list of functions to be called
CQS
"""
from abc import ABC
from enum import Enum
from types import TracebackType
from typing import Any, Optional, Self, Type


class WhatToQuery(int, Enum):
    """
    What to query class based on Python built-in Enum
    """

    ATTACK: int = 1
    DEFENSE: int = 2


class Query:
    """
    Query class.
    """

    def __init__(
        self,
        creature_name: str,
        what_to_query: WhatToQuery,
        default_value: int,
    ):
        self.creature_name: str = creature_name
        self.what_to_query: WhatToQuery = what_to_query
        self.value: int = default_value


class Event(list[Any]):
    """
    Event class based on Python built-in list.
    """

    def __call__(
        self, *args: tuple[Any, ...], **kwargs: dict[str, Any]
    ) -> None:
        for item in self:
            item(*args, **kwargs)


class Game:
    """
    Game class.
    """

    def __init__(self) -> None:
        self.queries: Event = Event()

    def perform_query(self, sender: Any, query: Any) -> None:
        """
        Performs a query
        :param sender: The sender of the query
        :type sender: Creature
        :param query: The query itself
        :type query: Query
        :return: None
        :rtype: NoneType
        """
        self.queries(sender, query)


class Creature:
    """
    Creature class
    """

    def __init__(self, game: Game, name: str, attack: int, defense: int):
        self.game: Game = game
        self.name: str = name
        self.initial_attack: int = attack
        self.initial_defense: int = defense

    @property
    def attack(self) -> int:
        """
        The getter method for attack attribute.
        :return: The attack
        :rtype: int
        """
        query: Query = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, query)
        return query.value

    @property
    def defense(self) -> int:
        """
        The getter method for defense attribute.
        :return: The defense
        :rtype: int
        """
        query: Query = Query(
            self.name, WhatToQuery.DEFENSE, self.initial_defense
        )
        self.game.perform_query(self, query)
        return query.value

    def __str__(self) -> str:
        return f"{self.name}: ({self.attack}/{self.defense})"


class CreatureModifier(ABC):
    """
    Creature Modifier that inherits from Abstract Base Class.
    """

    def __init__(self, game: Game, creature: Creature):
        self.creature: Creature = creature
        self.game: Game = game
        self.game.queries.append(self.handle)

    def handle(self, sender: Creature, query: Query) -> None:
        """
        Handle the query
        :param sender: The sender of the query
        :type sender:
        :param query: The query to perform
        :type query:
        :return: None
        :rtype: NoneType
        """

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    """
    Double Attack Modifier class that inherits from Creature Modifier.
    """

    def handle(self, sender: Creature, query: Query) -> None:
        if (
            sender.name == self.creature.name
            and query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value *= 2


if __name__ == "__main__":
    my_game: Game = Game()
    goblin: Creature = Creature(my_game, "Strong Goblin", 2, 2)
    print(goblin)
    with DoubleAttackModifier(my_game, goblin):
        print(goblin)
    print(goblin)
