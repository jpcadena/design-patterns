"""
A module for strategy in the gamma categorization.behavioral.strategy package.
"""
from abc import ABC
from enum import Enum, auto


class OutputFormat(Enum):
    """
    Output format for Strategy
    """

    MARKDOWN = auto()
    HTML = auto()


# not required but a good idea
class ListStrategy(ABC):
    """
    List strategy that inherits from Abstract Base Class
    """

    def start(self, buffer: list[str]) -> None:
        """
        Start the list strategy
        :param buffer: The buffer to start the list of items
        :type buffer: list[str]
        :return: None
        :rtype: NoneType
        """
        pass

    def end(self, buffer: list[str]) -> None:
        """
        End the list strategy
        :param buffer: The buffer to end the list of items
        :type buffer: list[str]
        :return: None
        :rtype: NoneType
        """
        pass

    def add_list_item(self, buffer: list[str], item: str) -> None:
        """
        Add a list item to the list
        :param buffer: The buffer to add the item
        :type buffer: list[str]
        :param item: The item to add
        :type item: str
        :return: None
        :rtype: NoneType
        """
        pass


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer: list[str], item: str) -> None:
        buffer.append(f' * {item}\n')


class HtmlListStrategy(ListStrategy):
    def start(self, buffer: list[str]) -> None:
        buffer.append('<ul>\n')

    def end(self, buffer: list[str]) -> None:
        buffer.append('</ul>\n')

    def add_list_item(self, buffer: list[str], item: str) -> None:
        buffer.append(f'  <li>{item}</li>\n')


class TextProcessor:
    """
    Text Processor representation class
    """

    def __init__(
        self, list_strategy: ListStrategy = HtmlListStrategy()
    ) -> None:
        self.buffer: list[str] = []
        self.list_strategy: ListStrategy = list_strategy

    def append_list(self, items: list[str]) -> None:
        """
        Append a list of items
        :param items: The list of items to append
        :type items: list[str]
        :return: None
        :rtype: NoneType
        """
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, output_format: OutputFormat) -> None:
        """
        Set the output format
        :param output_format: The output format to set
        :type output_format: OutputFormat
        :return: None
        :rtype: NoneType
        """
        if output_format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif output_format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self) -> None:
        """
        The clear method of the buffer
        :return: None
        :rtype: NoneType
        """
        self.buffer.clear()

    def __str__(self) -> str:
        return ''.join(self.buffer)


if __name__ == '__main__':
    my_items: list[str] = ['foo', 'bar', 'baz']
    text_processor: TextProcessor = TextProcessor()
    text_processor.set_output_format(OutputFormat.MARKDOWN)
    text_processor.append_list(my_items)
    print(text_processor)
    text_processor.set_output_format(OutputFormat.HTML)
    text_processor.clear()
    text_processor.append_list(my_items)
    print(text_processor)
