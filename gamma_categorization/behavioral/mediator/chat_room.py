"""
A module for chat room in the gamma categorization.behavioral.mediator package.
"""

from typing import Optional


class Person:
    """
    Person class represents a person
    """

    def __init__(self, name: str):
        self.name: str = name
        self.chat_log: list[str] = []
        self.room: Optional[ChatRoom] = None

    def receive(self, sender: str, message: str) -> None:
        """
        Receive a message from the chat room
        :param sender: The name of the sender
        :type sender: str
        :param message: The message to send
        :type message: str
        :return: None
        :rtype: NoneType
        """
        log: str = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {log}")
        self.chat_log.append(log)

    def say(self, message: str) -> None:
        """
        Say a message in the chat room
        :param message: The message to say
        :type message: str
        :return: None
        :rtype: NoneType
        """
        if self.room:
            self.room.broadcast(self.name, message)

    def private_message(self, who: str, message: str) -> None:
        """
        Send a private message to someone in the chat room
        :param who: The person to send the message
        :type who: str
        :param message: The private message to send
        :type message: str
        :return: None
        :rtype: NoneType
        """
        if self.room:
            self.room.message(self.name, who, message)


class ChatRoom:
    """
    The Chat Room class representation
    """

    def __init__(self) -> None:
        self.people: list[Person] = []

    def broadcast(self, source: str, message: str) -> None:
        """
        Broadcast a message to the chat room
        :param source: The source message
        :type source: str
        :param message: The message to broadcast
        :type message: str
        :return: None
        :rtype: NoneType
        """
        for person in self.people:
            if person.name != source:
                person.receive(source, message)

    def join(self, person: Person) -> None:
        """
        Join into the chat room
        :param person: The person to join
        :type person: Person
        :return: None
        :rtype: NoneType
        """
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def message(self, source: str, destination: str, message: str) -> None:
        """
        The message delivery function
        :param source: The source of the message
        :type source: str
        :param destination: The message destination
        :type destination: str
        :param message: The message to send
        :type message: str
        :return: None
        :rtype: NoneType
        """
        for person in self.people:
            if person.name == destination:
                person.receive(source, message)


if __name__ == "__main__":
    room: ChatRoom = ChatRoom()
    john: Person = Person("John")
    jane: Person = Person("Jane")
    room.join(john)
    room.join(jane)
    john.say("hi room")
    jane.say("oh, hey john")
    simon: Person = Person("Simon")
    room.join(simon)
    simon.say("hi everyone!")
    jane.private_message("Simon", "glad you could join us!")
