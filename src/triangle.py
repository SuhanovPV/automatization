import math

from src.figure import Figure


class Triangle(Figure):
    """Create figure class"""

    def __init__(self, side_a, side_b, side_c):
        self.triangle_validate(side_a, side_b, side_c)
        self.name = "Triangle"
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_area(self):
        """calculate area by three sides"""
        half_perimeter = self.perimeter / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.side_a) * (half_perimeter - self.side_b) *
                         (half_perimeter - self.side_c))

    def get_perimeter(self):
        """calculate perimeter"""
        return self.side_a + self.side_b + self.side_c

    @staticmethod
    def triangle_validate(*sides):
        """Validate possibility to create triangle"""
        if sides[0] + sides[1] <= sides[2] or \
                sides[1] + sides[2] <= sides[0] or \
                sides[0] + sides[2] <= sides[1] or \
                sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
            raise ValueError("Triangle can't be created!")


if __name__ == "__main__":
    t = Triangle(13, 14, 15)
