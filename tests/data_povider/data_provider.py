"""Generate data"""

import random


def generate_single_list(num):
    """generate list with random int values and len == num"""
    return [int(random.random() * 100 - 1) for x in range(num)]


def generate_coupe_list(num):
    """generate list of tuple with random int values and len == num. Len of tuple is 2"""
    return [(int(random.random() * 100 - 1), int(random.random() * 100 - 1)) for x in range(num)]


def generate_triangle_sides(num):
    counter = 0
    iter_counter = 0
    list_with_data = []
    while counter < num:
        iter_counter += 1
        side1 = int(random.random() * 50 - 1)
        side2 = int(random.random() * 50 - 1)
        side3 = int(random.random() * 50 - 1)

        if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
            counter += 1
            list_with_data.append((side1, side2, side3))
    return list_with_data
