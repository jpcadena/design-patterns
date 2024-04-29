"""
A module for events in the gamma categorization.behavioral.mediator package.
"""

from typing import Any


class Event(list[Any]):
    """
    A class for soccer events
    """

    def __call__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        for item in self:
            item(*args, **kwargs)


class Game:
    """
    A class for games at soccer event
    """

    def __init__(self) -> None:
        self.events = Event()

    def fire(self, args: tuple[Any, ...]) -> None:
        """
        A fire in the current game
        :param args: The tuple of arguments to fire
        :type args: tuple[Any, ...]
        :return: None
        :rtype: NoneType
        """
        self.events(*args)


class GoalScoredInfo:
    """
    Goal scored information at game
    """

    def __init__(self, who_scored: str, goals_scored: int) -> None:
        self.goals_scored: int = goals_scored
        self.who_scored: str = who_scored


class Player:
    """
    Player class representation
    """

    def __init__(self, name: str, game: Game) -> None:
        self.name: str = name
        self.game: Game = game
        self.goals_scored: int = 0

    def score(self) -> None:
        """
        Score a goal by given player
        :return: None
        :rtype: NoneType
        """
        self.goals_scored += 1
        args: GoalScoredInfo = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire((args,))


class Coach:
    """
    Soccer coach representation
    """

    def __init__(self, game: Game) -> None:
        game.events.append(self.celebrate_goal)

    @staticmethod
    def celebrate_goal(args: GoalScoredInfo) -> None:
        """
        Celebration of goal
        :param args: The arguments to celebrate the goal
        :type args: GoalScoredInfo
        :return: None
        :rtype: NoneType
        """
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f"Coach says: well done, {args.who_scored}!")


if __name__ == "__main__":
    my_game: Game = Game()
    player: Player = Player("Sam", my_game)
    coach: Coach = Coach(my_game)
    player.score()  # Coach says: well done, Sam!
    player.score()  # Coach says: well done, Sam!
    player.score()  # ignored by coach
