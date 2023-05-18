"""
Façade script
"""
from typing import Union


class Buffer:
    """
    Buffer class
    """

    def __init__(self, width: int = 30, height: int = 20):
        self.width: int = width
        self.height: int = height
        self.buffer: list[str] = [" "] * (width * height)

    def __getitem__(self, item: Union[int, slice]) -> Union[str, list[str]]:
        return self.buffer.__getitem__(item)

    def write(self, text: str) -> None:
        """
        Write text to the buffer
        :param text: The text to write
        :type text: str
        :return: None
        :rtype: NoneType
        """
        self.buffer += text


class Viewport:
    """
    Viewport class
    """

    def __init__(self, buffer: Buffer = Buffer()):
        self.buffer: Buffer = buffer
        self.offset: int = 0

    def get_char_at(self, index: int) -> str:
        """
        Get the character at position
        :param index: The index of the character
        :type index: int
        :return: The character at position
        :rtype: str
        """
        return self.buffer[index + self.offset]

    def append(self, text: str) -> None:
        """
        Append the text to the buffer
        :param text: The text to append
        :type text: str
        :return: None
        :rtype: NoneType
        """
        self.buffer.write(text)


class Console:
    """
    Console class
    """

    def __init__(self) -> None:
        buffer: Buffer = Buffer()
        self.viewport: Viewport = Viewport(buffer)
        self.buffers: list[Buffer] = [buffer]
        self.viewports: list[Viewport] = [self.viewport]

    def write(self, text: str) -> None:
        """
        Write text to the buffer through the console
        :param text: The text to write
        :type text: str
        :return: None
        :rtype: NoneType
        """
        self.viewport.buffer.write(text)

    def get_char_at(self, index: int) -> str:
        """
        Get the character at position
        :param index: The index of the character
        :type index: int
        :return: The character at position
        :rtype: str
        """
        return self.viewport.get_char_at(index)


if __name__ == "__main__":
    console: Console = Console()
    console.write("hello")
    character: str = console.get_char_at(0)
    print(character)
