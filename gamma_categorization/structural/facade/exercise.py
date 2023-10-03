"""
Façade Coding Exercise
"""
import secrets


class Generator:
    """
    Generator class
    """

    @staticmethod
    def generate(count: int) -> list[int]:
        """
        Generates a list of random numbers
        :param count: The count of random numbers to generate
        :type count: int
        :return: The list of random numbers
        :rtype: list[int]
        """
        return [secrets.choice(range(1, 10)) for _ in range(count)]


class Splitter:
    """
    Splitter class
    """

    @staticmethod
    def split(array: list[list[int]]) -> list[list[int]]:
        """
        Splits an array into a list of integers
        :param array: The array to split1
        :type array: list
        :return: The list of integers
        :rtype: list[list]
        """
        result: list[list[int]] = []
        row_count: int = len(array)
        col_count: int = len(array[0])
        for row in range(row_count):
            the_row: list[int] = []
            for col in range(col_count):
                the_row.append(array[row][col])
            result.append(the_row)
        for col in range(col_count):
            the_col: list[int] = []
            for row in range(row_count):
                the_col.append(array[row][col])
            result.append(the_col)
        diag1: list[int] = []
        diag2: list[int] = []
        for col in range(col_count):
            for row in range(row_count):
                if col == row:
                    diag1.append(array[row][col])
                row2: int = row_count - row - 1
                if col == row2:
                    diag2.append(array[row][col])
        result.append(diag1)
        result.append(diag2)
        return result


class Verifier:
    """
    Verifier class
    """

    @staticmethod
    def verify(arrays: list[list[int]]) -> bool:
        """
        Verifies the given arrays
        :param arrays: The list of arrays to verify
        :type arrays: list[list]
        :return: False if sum of arrays is different from the sum of
         the first array; otherwise True
        :rtype: bool
        """
        first: int = sum(arrays[0])
        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False
        return True


class MagicSquareGenerator:
    """
    Magic Square Generator class
    """

    @staticmethod
    def generate(size: int) -> list[list[int]]:
        """
        Generates the magic square
        :param size: The size of the square
        :type size: int
        :return: The magic square
        :rtype:  list[list[int]]
        """
        generator: Generator = Generator()
        splitter: Splitter = Splitter()
        verifier: Verifier = Verifier()
        while True:
            square: list[list[int]] = [
                generator.generate(size) for _ in range(size)
            ]
            split_square: list[list[int]] = splitter.split(square)
            if verifier.verify(split_square):
                return square


if __name__ == "__main__":
    magic_square_generator: MagicSquareGenerator = MagicSquareGenerator()
    magic_square: list[list[int]] = magic_square_generator.generate(3)
    for m_s in magic_square:
        print(m_s)
