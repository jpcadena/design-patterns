"""
A module for exercise in the gamma categorization.behavioral.mediator package.
"""


class Mediator:
    """
    Mediator class representation for system class
    """

    def __init__(self) -> None:
        self.participants: list[Participant] = []

    def add_participant(self, participant: 'Participant') -> None:
        """
        Add a participant to the list of participants for the mediator
        :param participant: The participant to add
        :type participant: Participant
        :return: None
        :rtype: NoneType
        """
        self.participants.append(participant)

    def broadcast(self, sender: 'Participant', value: int) -> None:
        """
        Broadcast the value by the sender to the class
        :param sender: The participant to broadcast the value
        :type sender: Participant
        :param value: The value given by the sender
        :type value: int
        :return: None
        :rtype: NoneType
        """
        for participant in self.participants:
            if participant != sender:
                participant.value += value


class Participant:
    """
    Participant class representation at system class
    """

    def __init__(self, mediator: Mediator):
        self.value: int = 0
        self.mediator: Mediator = mediator
        self.mediator.add_participant(self)

    def say(self, value: int) -> None:
        """
        Say a value in the class as a broadcast
        :param value: The value given by the participant
        :type value: int
        :return: None
        :rtype: NoneType
        """
        self.mediator.broadcast(self, value)
