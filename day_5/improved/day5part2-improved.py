from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
import string


def do_pass(line, deleted_polymer):
    stack = []
    for char in line:
        if char == deleted_polymer or char == deleted_polymer.upper():
            continue

        peek = stack[-1] if stack else None
        if peek:
            matching = char.lower() if char.isupper() else char.upper()
            if peek == matching:
                stack.pop()
                continue
        stack.append(char)

    return len(stack)


@timeit
def get_solution():
    return min(map(lambda polymer: do_pass(input_string(), deleted_polymer=polymer), string.ascii_lowercase))


print(get_solution())
