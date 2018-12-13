from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *


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

        output = rules.get(group, None)
        if output is None:
            if i < 0 or i >= len(pots):
                new_field += "."
            else:
                new_field += "."  # group[2]
        else:
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

    for _ in range(20):
        pots, zero_index = do_generation(pots, rules, zero_index)
        print(pots)
        print(zero_index)
    # print(pots)
    print(zero_index)

    total = sum([i - zero_index for i, item in enumerate(pots) if item == "#"])
    return total


print(get_solution())
