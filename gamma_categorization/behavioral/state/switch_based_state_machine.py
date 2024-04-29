"""
A module for switch based state machine in the gamma
 categorization.behavioral.state package.
"""

from enum import Enum, auto


class State(Enum):
    """Enumeration for States."""

    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


if __name__ == "__main__":
    code: str = "1234"
    state: State = State.LOCKED
    entry: str = ""
    while True:
        match state:
            case State.LOCKED:
                entry += input(f"Current entry: {entry}")
                if entry == code:
                    state = State.UNLOCKED
                elif not code.startswith(entry):
                    state = State.FAILED
            case State.FAILED:
                print("\nFAILED")
                entry = ""
                state = State.LOCKED
            case State.UNLOCKED:
                print("\nUNLOCKED")
                break
