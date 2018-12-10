from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *

from collections import defaultdict
import re


class Point:
    def __init__(self, line):
        string_pairs = re.findall('<(.*?)>', line)
        self.start_x, self.start_y = [int(item) for item in string_pairs[0].split(", ")]
        self.vel_x, self.vel_y = [int(item) for item in string_pairs[1].split(", ")]

        self.x, self.y = self.start_x, self.start_y

        print("pos: ({0}, {1}) vel: ({2}, {3})".format(self.start_x, self.start_y, self.vel_x, self.vel_y))

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)


def get_field_bounds(points):
    x_max = -1000000000000
    y_max = -1000000000000
    x_min = 1000000000000
    y_min = 1000000000000
    for point in points:
        if point.x < x_min:
            x_min = point.x
        if point.x > x_max:
            x_max = point.x
        if point.y < y_min:
            y_min = point.y
        if point.y > y_max:
            y_max = point.y

    return x_min, x_max, y_min, y_max


def print_field(points, bounds=None):

    if bounds is None:
        bounds = get_field_bounds(points)

    lines = []
    for y in range_inclusive(bounds[2], bounds[3]):
        line = []
        for x in range_inclusive(bounds[0], bounds[1]):
            item = "."
            for point in points:
                if point.x == x and point.y == y:
                    item = "#"
            line.append(item)
        lines.append("".join(line))
    print("\n".join(lines))


@timeit
def get_solution():
    points = [Point(line) for line in input_lines()]
    print("There are {0} points.".format(len(points)))

    bounds = get_field_bounds(points)
    print(bounds)
    input("Wait...")

    seconds = 0
    while True:
        x = defaultdict(int)
        y = defaultdict(int)
        for point in points:
            x[point.x] += 1
            y[point.y] += 1

        largest_x = max(x.values())
        largest_y = max(y.values())

        if largest_x >= 15 or largest_y >= 15:
            print(points)
            print(seconds)
            print_field(points)
            input("Wait...")
        for point in points:
            point.move()
        seconds += 1


print(get_solution())
