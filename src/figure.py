"""Figure class"""


class Figure:
    """Common class for figures"""

    def __init__(self):
        self.area = None

    def add_area(self, figure):
        """Added figure area to instance area"""
        self.validate_figure(figure)
        return self.area + figure.area

    @staticmethod
    def validate_figure(figure):
        """validate is object is figure instance"""
        if not isinstance(figure, Figure):
            raise ValueError(f"{figure} is not {Figure}")
