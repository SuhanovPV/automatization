"""Test figures"""

import math
import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from tests.data_povider.data_provider import generate_coupe_list, generate_single_list, generate_triangle_sides


@pytest.mark.parametrize("side_a, side_b", generate_coupe_list(3))
def test_rectangle_creation(side_a, side_b):
    """Test rectangle creation"""
    test_name = "Rectangle"
    test_rectangle = Rectangle(side_a, side_b)

    assert test_rectangle.name == test_name
    assert test_rectangle.perimeter == (side_a + side_b) * 2
    assert test_rectangle.area == side_a * side_b


@pytest.mark.parametrize("side", generate_single_list(3))
def test_creation_square(side):
    """Test Square creation"""
    square_name = "Square"
    test_square = Square(side)
    assert test_square.area == side ** 2
    assert test_square.perimeter == side * 4
    assert test_square.name == square_name


@pytest.mark.parametrize("radius", generate_single_list(3))
def test_creation_circle(radius):
    """Test Circle creation"""
    circle_name = "Circle"
    test_circle = Circle(radius)
    assert test_circle.area == (radius ** 2) * math.pi
    assert test_circle.perimeter == 2 * math.pi * radius
    assert test_circle.name == circle_name


@pytest.mark.parametrize("side_a, side_b, side_c", generate_triangle_sides(3))
def test_create_triangle_positive(side_a, side_b, side_c):
    """Test triangle creation"""
    triangle_name = "Triangle"
    test_triangle = Triangle(side_a, side_b, side_c)
    assert test_triangle.name == triangle_name
    assert test_triangle.perimeter == side_a + side_b + side_c

    half_perimeter = (side_a + side_b + side_c) / 2
    assert test_triangle.area == math.sqrt(half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) *
                                           (half_perimeter - side_c))


@pytest.mark.parametrize("side_a, side_b, side_c", [(-2, -5, 15), (0, 2, 4), (5, 15, -5)])
def test_create_triangle_negative(side_a, side_b, side_c):
    """Check exception ValueError, if there is can not create triangle by three sides"""
    with pytest.raises(ValueError):
        test_triangle = Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize("fig_1", [
    Rectangle(3, 4),
    Square(3),
    Circle(5),
    Triangle(3, 4, 6)])
@pytest.mark.parametrize("fig_2", [
    Rectangle(3, 4),
    Square(3),
    Circle(5),
    Triangle(3, 4, 6)])
def test_figure_area_with_adding_figure(fig_1, fig_2):
    assert fig_1.add_area(fig_2) == fig_1.area + fig_2.area, \
        f"{fig_1.name} area + {fig_2.area} is {fig_1.area + fig_2.area}, but function return {fig_1.add_area(fig_2)}"


@pytest.mark.parametrize("fig", [
    Rectangle(3, 4),
    Square(3),
    Circle(5),
    Triangle(3, 4, 6)])
@pytest.mark.parametrize("val", ["str", 10, 2.3, None, True])
def test_figure_area_with_adding_figure(fig, val):
    with pytest.raises(ValueError):
        fig.add_area(val)
