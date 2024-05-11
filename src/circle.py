"""Circle class"""
import math

from src.figure import Figure


class Circle(Figure):
    """Create circle class"""

    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self) -> float:
        """calculate circle area by radius"""
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        """calculate circle perimeter"""
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(2)
    print(c.get_area())
    print(c.get_perimeter())
    print(c.name)
