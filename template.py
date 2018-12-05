from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from collections import defaultdict
import string
import time


def get_lines():
    with open("input.txt") as fp:
        return [line[:-1] for line in fp]


@timeit
def get_solution():
    data = input_lines()


print(get_solution())
