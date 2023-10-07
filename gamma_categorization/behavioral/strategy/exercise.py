"""
A module for exercise in the gamma categorization.behavioral.strategy package.
"""
from abc import ABC, abstractmethod
from cmath import sqrt


class DiscriminantStrategy(ABC):
    """
    Discriminant Strategy representation from Abstract Base Class
    """

    @abstractmethod
    def calculate_discriminant(self, a: float, b: float, c: float) -> float:
        """
        Calculates the discriminant for an equation
        :param a: Coefficient a
        :type a: float
        :param b: Coefficient b
        :type b: float
        :param c: Coefficient c
        :type c: float
        :return: The discriminant of the equation
        :rtype: float
        """
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a: float, b: float, c: float) -> float:
        return b**2 - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a: float, b: float, c: float) -> float:
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return float('nan')
        return discriminant


class QuadraticEquationSolver:
    """
    Quadratic Equation Solver class
    """

    def __init__(self, strategy: DiscriminantStrategy):
        self.strategy = strategy

    def solve(self, a: float, b: float, c: float) -> tuple[complex, complex]:
        """Returns a pair of complex (!) values"""
        discriminant = self.strategy.calculate_discriminant(a, b, c)
        root_discriminant = sqrt(discriminant)

        return (
            (-b + root_discriminant) / (2 * a),
            (-b - root_discriminant) / (2 * a),
        )


if __name__ == "__main__":
    # Using ordinary discriminant strategy
    solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
    solutions = solver.solve(1, 10, 16)
    print("Ordinary Discriminant Strategy:", solutions)

    # Using real discriminant strategy
    solver = QuadraticEquationSolver(RealDiscriminantStrategy())
    solutions = solver.solve(1, 4, 5)
    print("Real Discriminant Strategy:", solutions)
