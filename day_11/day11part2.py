from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *

import itertools


# From https://gist.github.com/SiestaMadokaist/74e573365a02f5d914d2
class SummedAreaTable(object):
    def __init__(self, size, data):
        """
        Just because I dislike a 2d array / list.
        data should be a List of Integer.
        """
        self.width, self.height = size
        assert self.width * self.height == len(data), "invalid data length and or data size"
        self.size = size
        self.data = data
        self.memo = [None for _ in range(self.width * self.height)]
        self._generate()

    def get(self, x, y):
        """
        get the value of self, at point x, y.
        it's possible for the value at that point hadn't been generated.
        """
        index = y * self.width + x
        stored = self.memo[index]

        if x < 0 or y < 0:
            # value at negative-indexed point is always 0
            return 0
        elif stored is not None:
            # if the value at point x, y has already been generated
            return stored
        else:
            # calculate the value at point x, y if it hasn't been generated
            cumulative = self.get(x - 1, y) + self.get(x, y - 1) - self.get(x - 1, y - 1) + self.data[index]
            self.memo[index] = cumulative
            return cumulative

    def total(self, x0, y0, x1, y1):
        """
        get the cumulative value of this instance from point (x0, y0) to (x1, y1)
        """
        a = self.get(x0 - 1, y0 - 1)
        b = self.get(x0 - 1, y1)
        c = self.get(x1, y0 - 1)
        d = self.get(x1, y1)

        return d - b - c + a

    def _generate(self):
        self.memo = [self.get(x, y) for y in range(self.height) for x in range(self.width)]


def get_power_level(x, y, serial):
    rack_id = x + 10
    power_level = ((rack_id * y) + serial) * rack_id
    power_str = str(power_level)
    if len(power_str) >= 3:
        # Keep hundreds digit
        power_level = int(power_str[-3])
    else:
        power_level = 0

    power_level -= 5
    return power_level


def get_max_power(power, max_square_size, grid_size):
    largest_value = 0
    largest_index = (-1, -1, 0)

    flattened = list(itertools.chain(*power))
    table = SummedAreaTable((grid_size, grid_size), data=flattened)

    for size in range(max_square_size):
        for y in range(grid_size - size):
            for x in range(grid_size - size):
                total = table.total(x, y, x + size, y + size)
                # print("({0}, {1}) for {2} += {3}".format(x, y, size, total))
                # print(total)

                if total > largest_value:
                    largest_value = total
                    largest_index = (x, y, size)

    return largest_index, largest_value


@timeit
def get_solution():
    serial = 1788
    grid_size = 300
    max_square_size = 300

    power = [[get_power_level(x, y, serial) for x in range_inclusive(1, grid_size)]
             for y in range_inclusive(1, grid_size)]

    largest_index, largest_value = get_max_power(power, max_square_size, grid_size)
    print("({0}, {1}) had the most power ({2}) with a square size of {3}".format(
        largest_index[0] + 1,
        largest_index[1] + 1,
        largest_value,
        largest_index[2] + 1
    ))
    return "{0},{1},{2}".format(largest_index[0] + 1, largest_index[1] + 1, largest_index[2] + 1)


print(get_solution())
