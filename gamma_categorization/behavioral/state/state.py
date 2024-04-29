"""
A module for state in the gamma categorization.behavioral.state package.
"""

# interesting but not practical :)
from abc import ABC


class Switch:
    """
    Switch class representation
    """

    def __init__(self) -> None:
        self.state: State = OffState()

    def on(self) -> None:
        """
        Turns the switch on.
        :return: None
        :rtype: NoneType
        """
        self.state.on(self)

    def off(self) -> None:
        """
        Off the state
        :return: None
        :rtype: NoneType
        """
        self.state.off(self)


class State(ABC):
    """
    State representation from Abstract Base Class
    """

    def on(self, switch: Switch) -> None:
        """
        Turns the switch off.
        :param switch: The switch state
        :type switch: Switch
        :return: None
        :rtype: NoneType
        """
        print("Light is already on")

    def off(self, switch: Switch) -> None:
        """
        Off switch state
        :param switch: The switch state
        :type switch: Switch
        :return: None
        :rtype: NoneType
        """
        print("Light is already off")


class OnState(State):
    def __init__(self) -> None:
        print("Light turned on")

    def off(self, switch: Switch) -> None:
        print("Turning light off...")
        switch.state = OffState()


class OffState(State):
    def __init__(self) -> None:
        print("Light turned off")

    def on(self, switch: Switch) -> None:
        print("Turning light on...")
        switch.state = OnState()


if __name__ == "__main__":
    my_switch: Switch = Switch()
    my_switch.on()  # Turning light on...
    # Light turned on
    my_switch.off()  # Turning light off...
    # Light turned off
    my_switch.off()  # Light is already off
