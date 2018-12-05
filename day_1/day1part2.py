from collections import defaultdict


def get_lines():
    with open("input.txt") as fp:
        return [eval(line) for line in fp]


def get_solution():
    total = 0

    freqs = defaultdict(int)
    freqs[0] = 1

    lines = get_lines()

    while True:
        for item in lines:
            total += item

            if freqs[total] != 0:
                return total

            freqs[total] += 1

    return "No repeats"


print(get_solution())
