from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *

import itertools


def get_power_level(x, y, serial):
    rackid = x + 10
    level = rackid * y
    level += serial
    level *= rackid
    level = (level // 100) % 10
    level -= 5
    return level


@timeit
def get_solution():
    serial = 1788
    grid_size = 300
    max_square_size = 300

    sums = [[0 for _ in range(grid_size + 1)] for _ in range(grid_size + 1)]

    for y in range_inclusive(1, 300):
        for x in range_inclusive(1, 300):
            sums[y][x] = sums[y][x - 1] + sums[y - 1][x] - sums[y - 1][x - 1] + get_power_level(x, y, serial)

    largest_index = (-1, -1)
    largest_size = -1
    largest_level = -1000000000

    for s in range(max_square_size):
        for y in range_inclusive(1, grid_size - s):
            for x in range_inclusive(1, grid_size - s):
                level = sums[y + s][x + s] - sums[y + s][x - 1] - sums[y - 1][x + s] + sums[y - 1][x - 1]
                if level > largest_level:
                    largest_index = (x, y)
                    largest_size = s + 1
                    largest_level = level

    return "{0} had the most power ({1}) with a square size of {2}".format(
        largest_index,
        largest_level,
        largest_size
    )


print(get_solution())
