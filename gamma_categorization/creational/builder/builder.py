"""
Builder script
"""

from typing import Any

# text: str = 'hello'
# parts: list[str] = ['<p>', text, '</p>']
# print(''.join(parts))
#
# words: list[str] = ['hello', 'world']
# parts: list[str] = ['<ul>']
# for word in words:
#     parts.append(f' <li>{word}</li>')
# parts.append('</ul>')
# print('\n'.join(parts))


class HtmlElement:
    """
    HTML Element class
    """

    indent_size: int = 2

    def __init__(self, name: str = "", text: str = ""):
        self.name: str = name
        self.text: str = text
        self.elements: list[Any] = []

    def __str__(self, indent: int = 0) -> str:
        lines: list[str] = []
        i: str = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")
        if self.text:
            text_indent: str = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{text_indent}{self.text}")
        for element in self.elements:
            lines.append(element.__str__(indent + 1))
        lines.append(f"{i}</{self.name}")
        return "\n".join(lines)

    # @staticmethod
    # def create(name: str):
    #     return HTMLBuilder(name)


class HtmlBuilder:
    """
    HTML Builder class
    """

    def __init__(self, root_name: str):
        self.root_name: str = root_name
        self.__root: HtmlElement = HtmlElement(root_name)

    def add_child(self, child_name: str, child_text: str) -> None:
        """
        Add a child element for HTML element
        :param child_name: Name of the child element
        :type child_name: str
        :param child_text: Text of the child element
        :type child_text: str
        :return: None
        :rtype: NoneType
        """
        self.__root.elements.append(HtmlElement(child_name, child_text))
        # return self  # to apply chained method "fluently"

    def __str__(self) -> str:
        return str(self.__root)


html_builder: HtmlBuilder = HtmlBuilder("ul")
html_builder.add_child("li", "hello")
html_builder.add_child("li", "world")
print("Ordinary builder")
print(html_builder)
