from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *

from collections import defaultdict
from collections import Counter
import string
import time
from pprint import pprint


def do_generation(pots, rules, zero_index):
    """
    Field can grow by 2 at most on either side for each generation
    pass
    (| is left side of "current" pots set)
    ...|## => #
    ...|#. => #
    ....|# => #

    So we need to evaluate rules for -1, -2, +1, and +2 compared to boundaries
    """

    field = ("." * 4) + pots + ("." * 4)
    zero_index += 2
    new_field = ""

    for i in range(-2, len(pots) + 2):
        j = i + 4
        group = field[j-2:j+3]

        output = rules.get(group, ".")
        new_field += output

    return new_field, zero_index


@timeit
def get_solution():

    lines = input_lines("input.txt")
    pots = lines[0].split(": ")[1]
    print(pots)

    rules = {}
    for item in lines[2:]:
        terms = item.split(" => ")
        lhs = terms[0]
        rhs = terms[1]
        rules[lhs] = rhs

    zero_index = 0
    last_total = -1
    last_diff = -1

    first_repeating_iteration = -1

    goal_iteration = 50000000000  # Change to 20 for day 12 part 1

    for iteration in range_inclusive(1, goal_iteration):
        """
        Eventually, the difference in the total between one generation and the next will be constant.
        Figure out when this stabilization occurs, and use simple math to extrapolate the result at
        50 billion iterations.
        """
        pots, zero_index = do_generation(pots, rules, zero_index)
        print(pots)

        total = sum([i - zero_index for i, item in enumerate(pots) if item == "#"])

        diff = total - last_total
        print("iteration {0} had diff of {1}".format(iteration, diff))
        print("total: {0}, last: {1}".format(total, last_total))

        if iteration == goal_iteration:
            return total

        if diff == last_diff:
            first_repeating_iteration = iteration - 1
            print("-----------------------")
            print("Rate of growth has stabilized at iteration {0} with a value of {1}".format(first_repeating_iteration, last_diff))
            break

        last_total = total
        last_diff = diff

    remaining_iterations = goal_iteration - first_repeating_iteration
    return (remaining_iterations * last_diff) + last_total


print(get_solution())
