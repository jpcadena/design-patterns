"""
Flyweight script using a Text Formatting
"""
from typing import Any


class FormattedText:
    """
    Formatted Text class
    """

    def __init__(self, plain_text: str):
        self.plain_text: str = plain_text
        self.caps: list[bool] = [False] * len(plain_text)

    def capitalize(self, start: int, end: int) -> None:
        """
        Capitalize a string
        :param start: The first character to capitalize
        :type start: int
        :param end: The last character to capitalize
        :type end: int
        :return: None
        :rtype: NoneType
        """
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self) -> str:
        result: list[str] = []
        for idx, value in enumerate(self.caps):
            char: str = self.plain_text[idx]
            result.append(char.upper() if value else char)
        return "".join(result)


class BetterFormattedText:
    """
    Better Formatted Text class
    """

    def __init__(self, plain_text: str):
        self.plain_text: str = plain_text
        self.formatting: list[Any] = []

    class TextRange:
        """
        Text Range class
        """

        def __init__(self, start: int, end: int, capitalize: bool = False):
            self.start: int = start
            self.end: int = end
            self.capitalize: bool = capitalize

        def covers(self, position: int) -> bool:
            """
            Covers a given position
            :param position: The position to cover
            :type position: int
            :return: True if the position is covered, False otherwise
            :rtype: bool
            """
            return self.start <= position <= self.end

    def get_range(self, start: int, end: int) -> TextRange:
        """
        Get the range of the text
        :param start: The start of the text
        :type start: int
        :param end: The end of the text
        :type end: int
        :return: The text range
        :rtype: TextRange
        """
        text_range = self.TextRange(start, end)
        self.formatting.append(text_range)
        return text_range

    def __str__(self) -> str:
        result: list[str] = []
        for i, char in enumerate(self.plain_text):
            for rng in self.formatting:
                if rng.covers(i) and rng.capitalize:
                    char = char.upper()
            result.append(char)
        return "".join(result)


if __name__ == "__main__":
    text: str = "This is a brave new world"
    formatted_text: FormattedText = FormattedText(text)
    formatted_text.capitalize(10, 15)
    print(formatted_text)

    better_formatted_text: BetterFormattedText = BetterFormattedText(text)
    better_formatted_text.get_range(16, 19).capitalize = True
    print(better_formatted_text)
