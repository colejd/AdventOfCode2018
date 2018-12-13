from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *
from collections import Counter
from collections import defaultdict
import string
from pprint import pprint


def get_bounds(points):
    x_max = -1000000000000
    y_max = -1000000000000
    x_min = 1000000000000
    y_min = 1000000000000
    for point in points:
        if point[0] < x_min:
            x_min = point[0]
        if point[0] > x_max:
            x_max = point[0]
        if point[1] < y_min:
            y_min = point[1]
        if point[1] > y_max:
            y_max = point[1]

    return x_min, x_max, y_min, y_max


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


@timeit
def get_solution():
    input_strings = input_lines()
    region_points = list(map(lambda line: tuple([int(n) for n in line.split(", ")]), input_strings))
    bounds = get_bounds(region_points)

    print("Bounds: {0}".format(bounds))

    area = 0

    for y in range_inclusive(bounds[2], bounds[3]):
        for x in range_inclusive(bounds[0], bounds[1]):
            current_point = (x, y)

            # Get the distance of all input points from this point
            df = {i: manhattan_distance(v, current_point) for (i, v) in enumerate(region_points)}

            if sum(df.values()) < 10000:
                area += 1

    return area


print(get_solution())

# Answer is 35928
