"""Rectangle class"""
from src.figure import Figure


class Rectangle(Figure):
    """Create Rectangle figure"""

    def __init__(self, side_a, side_b):
        self.name = "Rectangle"
        self.side_a = side_a
        self.side_b = side_b
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self):
        """calculate rectangle area"""
        return self.side_a * self.side_b

    def get_perimeter(self):
        """calculate rectangle perimeter"""
        return (self.side_a + self.side_b) * 2


if __name__ == "__main__":
    r = Rectangle(2, 5)
    r2 = Rectangle(2, 5)
    print(r.name)
    print(r.get_area())
    print(r.get_perimeter())
    r.add_area(r2)
