from collections import defaultdict


def get_lines():
    with open("input.txt") as fp:
        return [line[:-1] for line in fp]


def get_solution():
    boxes = get_lines()

    two_count = 0
    three_count = 0

    for box in boxes:
        freqs = defaultdict(int)

        has_two = False
        has_three = False

        for char in box:
            freqs[char] += 1

        for key, value in freqs.items():
            if value == 2:
                has_two = True
            if value == 3:
                has_three = True

        if has_two:
            two_count += 1
        if has_three:
            three_count += 1

    return two_count * three_count


print(get_solution())
