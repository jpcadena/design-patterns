"""
Open-Closed Principle
"""
from enum import Enum
from typing import Any, Generator, Self


class Color(int, Enum):
    """
    Color class based on Enum
    """

    RED: int = 1
    GREEN: int = 2
    BLUE: int = 3


class Size(int, Enum):
    """
    Size class based on Enum
    """

    SMALL: int = 1
    MEDIUM: int = 2
    LARGE: int = 3


class Product:
    """
    Product class based on Product
    """

    def __init__(self, name: str, color: Color, size: Size):
        self.name: str = name
        self.color: Color = color
        self.size: Size = size


# Class with many filter methods with different specs is WRONG


class ProductFilter:
    """
    Product Filter class
    """

    def filter_by_color(
        self, products: list[Product], color: Color
    ) -> Generator[Product, Any, None]:
        """
        Filter by color method
        :param products: list of products
        :type products: list[Product]
        :param color: color enum
        :type color: Color
        :return: Product instance
        :rtype: Generator[Product, Any, None]
        """
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(
        self, products: list[Product], size: Size
    ) -> Generator[Product, Any, None]:
        """
        Filter by size method
        :param products: list of products
        :type products: list[Product]
        :param size: size enum
        :type size: Size
        :return: Product instance
        :rtype: Generator[Product, Any, None]
        """
        for product in products:
            if product.size == size:
                yield product

    def filter_by_size_and_color(
        self, products: list[Product], size: Size, color: Color
    ) -> Generator[Product, Any, None]:
        """
        Filter by size and color method
        :param products: list of products
        :type products: list[Product]
        :param size: size enum
        :type size: Size
        :param color: color enum
        :type color: Color
        :return: Product instance
        :rtype: Generator[Product, Any, None]
        """
        for product in products:
            if product.color == color and product.size == size:
                yield product

    # state space explosion
    # 3 criteria
    # c s w cs sw cw csw = 7 methods

    # OCP = open for extension, closed for modification


class Specification:
    """
    Specification class
    """

    def is_satisfied(self, item: Product) -> Any:
        """
        Is satisfied the product
        :param item: product
        :type item: Product
        :return: Some value
        :rtype: Any
        """

    # and operator makes life easier
    def __and__(self, other: Self) -> "AndSpecification":
        return AndSpecification(self, other)


class Filter:
    """
    Filter class
    """

    def filter(self, items: list[Product], spec: Specification) -> Any:
        """
        Filter method
        :param items: list of products
        :type items: list[Product]
        :param spec: specification to filter by
        :type spec: Specification
        :return: Some value
        :rtype: Any
        """


class ColorSpecification(Specification):
    """
    Color Specification class based on Specification
    """

    def __init__(self, color: Color):
        self.color: Color = color

    def is_satisfied(self, item: Product) -> bool:
        return item.color == self.color


class SizeSpecification(Specification):
    """
    Size Specification class based on Specification
    """

    def __init__(self, size: Size):
        self.size: Size = size

    def is_satisfied(self, item: Product) -> bool:
        return item.size == self.size


# class AndSpecification(Specification):
#     def __init__(self, spec1: Specification, spec2: Specification):
#         self.spec2: Specification = spec2
#         self.spec1: Specification = spec1
#
#     def is_satisfied(self, item: Product):
#         return self.spec1.is_satisfied(item) and \
#                self.spec2.is_satisfied(item)


class AndSpecification(Specification):
    """
    And Specification class based on Specification
    """

    def __init__(self, *args: Specification) -> None:
        self.args: tuple[Specification, ...] = args

    def is_satisfied(self, item: Product) -> bool:
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    """
    Better Filter class based on Filter
    """

    def filter(
        self, items: list[Product], spec: Specification
    ) -> Generator[Product, Any, None]:
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple: Product = Product("Apple", Color.GREEN, Size.SMALL)
tree: Product = Product("Tree", Color.GREEN, Size.LARGE)
house: Product = Product("House", Color.BLUE, Size.LARGE)

my_products: list[Product] = [apple, tree, house]

pf: ProductFilter = ProductFilter()
print("Green products (old):")
for p in pf.filter_by_color(my_products, Color.GREEN):
    print(f" - {p.name} is green")

# ^ BEFORE

# v AFTER
bf: BetterFilter = BetterFilter()

print("Green products (new):")
green: ColorSpecification = ColorSpecification(Color.GREEN)
for p in bf.filter(my_products, green):
    print(f" - {p.name} is green")

print("Large products:")
large: SizeSpecification = SizeSpecification(Size.LARGE)
for p in bf.filter(my_products, large):
    print(f" - {p.name} is large")

print("Large blue items:")
# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
large_blue: AndSpecification = AndSpecification(
    large, ColorSpecification(Color.BLUE)
)
for p in bf.filter(my_products, large_blue):
    print(f" - {p.name} is large and blue")
