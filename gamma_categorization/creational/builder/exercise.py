"""
Builder Coding Exercise
You are asked to implement the Builder design pattern for rendering
 simple chunks of code.
"""
from typing import Self

# Sample use of the builder you are asked to create:
#
# cb = CodeBuilder('Person').add_field('name', '""') \
#                           .add_field('age', '0')
# print(cb)
# The expected output of the above code is:
#
# class Person:
#   def __init__(self):
#     self.name = ""
#     self.age = 0


class CodeBuilder:
    """
    Code Builder class
    """

    INDENT_STEP = 2

    def __init__(self, root_name: str) -> None:
        self.root_name: str = root_name
        self.indent: int = 0
        self.fields: list[tuple[str, str]] = []

    def add_field(self, field_type: str, name: str) -> Self:
        """
        Method to add a field as class attributes
        :param field_type: Name of the attribute
        :type field_type: str
        :param name: Value of the attribute
        :type name: str
        :return: CodeBuilder instance
        :rtype: Self
        """
        self.fields.append((field_type, name))
        return self

    def __str__(self) -> str:
        if not self.fields:
            return f"class {self.root_name}:\n  pass"
        lines: list[str] = [
            f"class {self.root_name}:",
            "  def __init__(self):",
        ]
        self.indent += self.INDENT_STEP
        for field in self.fields:
            lines.append(f"    self.{field[0]} = {field[1]}")
        self.indent -= self.INDENT_STEP
        return "\n".join(lines)


code_builder: CodeBuilder = (
    CodeBuilder("Person").add_field("name", '""').add_field("age", "0")
)
print(code_builder)

# Change f'strings to format(vars) instead for UnitTest at Python 3.5
