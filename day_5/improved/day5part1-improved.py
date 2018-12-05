from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *


def do_pass(line):
    stack = []
    for char in line:
        peek = stack[-1] if stack else None
        if peek:
            matching = char.lower() if char.isupper() else char.upper()
            if peek == matching:
                stack.pop()
                continue
        stack.append(char)

    return stack


@timeit
def get_solution():
    return len(do_pass(input_string()))


print(get_solution())
