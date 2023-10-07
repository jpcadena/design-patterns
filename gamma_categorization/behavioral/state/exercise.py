"""
A module for exercise in the gamma categorization.behavioral.state package.
"""


class CombinationLock:
    """
    Combination lock class representation
    """

    def __init__(self, combination: list[int]) -> None:
        self.combination: list[int] = combination
        self.status: str = 'LOCKED'
        self.entered_digits: list[int] = []

    def reset(self) -> None:
        """
        Reset lock to LOCKED state
        :return: None
        :rtype: NoneType
        """
        self.status = 'LOCKED'
        self.entered_digits = []

    def enter_digit(self, digit: int) -> None:
        """
        Enter a digit into the lock
        :param digit: The digit to enter
        :type digit: int
        :return: None
        :rtype: NoneType
        """
        if self.status in ['LOCKED', 'ERROR']:
            self.reset()
        self.entered_digits.append(digit)
        self.status = ''.join(map(str, self.entered_digits))
        if self.entered_digits == self.combination:
            self.status = 'OPEN'
        elif len(self.entered_digits) == len(self.combination):
            self.status = 'ERROR'
