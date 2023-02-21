"""
Builder Coding Exercise
You are asked to implement the Builder design pattern for rendering
 simple chunks of code.
"""


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

    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.indent = 0
        self.fields = []

    def add_field(self, field_type, name):
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
            return "class {}:\n  pass".format(self.root_name)
        lines = ["class {}:".format(self.root_name), "  def __init__(self):"]
        self.indent += self.INDENT_STEP
        for field in self.fields:
            lines.append("    self.{} = {}".format(field[0], field[1]))
        self.indent -= self.INDENT_STEP
        return "\n".join(lines)


code_builder = CodeBuilder('Person').\
    add_field('name', '""').\
    add_field('age', '0')
print(code_builder)

# This code does not include f'string because of the UnitTest
# done with Python 3.5
