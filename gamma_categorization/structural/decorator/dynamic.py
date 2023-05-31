"""
Dynamic Decorator script
"""
from typing import Any, Iterator, TextIO


class FileWithLogging:
    """
    File with logging class.
    """

    def __init__(self, file: TextIO) -> None:
        self.file: TextIO = file

    def writelines(self, lines: list[str]) -> None:
        """
        Write lines to file
        :param lines: List of lines to write
        :type lines: list[str]
        :return: None
        :rtype: NoneType
        """
        self.file.writelines(lines)
        print(f"Writing {len(lines)} lines")

    def __iter__(self) -> Iterator[str]:
        return self.file.__iter__()

    def __next__(self) -> str:
        return self.file.__next__()

    def __getattr__(self, item: str) -> Any:
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "file":
            self.__dict__["file"] = value
        else:
            setattr(self.__dict__["file"], key, value)

    def __delattr__(self, item: str) -> None:
        delattr(self.__dict__["file"], item)


if __name__ == "__main__":
    with open("data/hello.txt", "w", encoding="utf-8") as opened_file:
        file_with_logging = FileWithLogging(opened_file)
        file_with_logging.writelines(["hello", ", ", "world!"])
        file_with_logging.write("\ntesting")
