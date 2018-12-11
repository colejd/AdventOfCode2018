from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *


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


def get_max_power(power, square_size):

    largest_value = 0
    largest_index = (-1, -1)

    for y in range(300 - (square_size - 1)):
        for x in range(300 - (square_size - 1)):
            total = 0
            for x_off in range(square_size):
                for y_off in range(square_size):
                    total += power[y + y_off][x + x_off]
            if total > largest_value:
                largest_value = total
                largest_index = (x, y)

    return largest_index, largest_value


@timeit
def get_solution():
    serial = 1788
    power = [[get_power_level(x, y, serial) for x in range_inclusive(1, 300)] for y in range_inclusive(1, 300)]

    largest_index, _ = get_max_power(power, 3)
    return "{0},{1}".format(largest_index[0] + 1, largest_index[1] + 1)


print(get_solution())
