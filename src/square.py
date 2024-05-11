from src.rectangle import Rectangle


class Square(Rectangle):
    """Create square class"""

    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


if __name__ == "__main__":
    s = Square(5)
    print(s.name)
    print(s.get_area())
    print(s.get_perimeter())
