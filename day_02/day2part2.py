from collections import defaultdict


def get_lines():
    with open("input.txt") as fp:
        return [line[:-1] for line in fp]


def get_solution():
    boxes = get_lines()

    for box in boxes:
        for other_box in boxes:
            if other_box == box:
                continue

            diff = 0
            diffchar = -1
            for i in range(len(box)):
                if box[i] != other_box[i]:
                    diff += 1
                    diffchar = i

            if diff == 1:
                return box[:diffchar] + box[diffchar + 1:]


print(get_solution())
