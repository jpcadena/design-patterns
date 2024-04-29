"""
A module for template in the gamma categorization.behavioral.template method
 package.
"""

from abc import ABC, abstractmethod


class Game(ABC):
    """
    Game representation from Abstract Base Class
    """

    def __init__(self, number_of_players: int) -> None:
        self.number_of_players: int = number_of_players
        self.current_player: int = 0

    def run(self) -> None:
        """
        Run the game
        :return: None
        :rtype: NoneType
        """
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} wins!")

    def start(self) -> None:
        """
        Start the game
        :return: None
        :rtype: NoneType
        """
        pass

    @abstractmethod
    @property
    def have_winner(self) -> bool:
        """
        Have a winner from the game
        :return: True if there's a winner; False if tied
        :rtype: bool
        """
        pass

    def take_turn(self) -> None:
        """
        Take turns in the game
        :return: None
        :rtype: NoneType
        """
        pass

    @abstractmethod
    @property
    def winning_player(self) -> int:
        """
        Winning player
        :return: The identifier for the winning player
        :rtype: int
        """
        pass


class Chess(Game):
    def __init__(self) -> None:
        super().__init__(2)
        self.max_turns: int = 10
        self.turn: int = 1

    def start(self) -> None:
        print(
            f"Starting a game of chess with {self.number_of_players} players."
        )

    @property
    def have_winner(self) -> bool:
        return self.turn == self.max_turns

    def take_turn(self) -> None:
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self) -> int:
        return self.current_player


if __name__ == "__main__":
    chess: Chess = Chess()
    chess.run()
