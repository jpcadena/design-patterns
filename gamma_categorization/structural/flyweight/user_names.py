"""
Flyweight script for Usernames
"""

import secrets
import string


class User:
    """
    User class
    """

    def __init__(self, name: str):
        self.name: str = name


class ImprovedUser:
    """
    Improved User class
    """

    strings: list[str] = []

    def __init__(self, full_name: str):
        def get_or_add(name: str) -> int:
            """
            Get or add a string
            :param name: The full name of the user
            :type name: str
            :return: The position of the user or the length of the string
            :rtype: int
            """
            if name in self.strings:
                return self.strings.index(name)
            self.strings.append(name)
            return len(self.strings) - 1

        self.names: list[int] = [
            get_or_add(name) for name in full_name.split(" ")
        ]

    def __str__(self) -> str:
        return " ".join(self.strings[name] for name in self.names)


def random_string() -> str:
    """
    Generate random string
    :return: The random string
    :rtype: str
    """
    return "".join([secrets.choice(string.ascii_lowercase) for _ in range(8)])


if __name__ == "__main__":
    users: list[ImprovedUser] = []
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]
    for first_name in first_names:
        for last_name in last_names:
            users.append(ImprovedUser(f"{first_name} {last_name}"))
    print(users[0])
