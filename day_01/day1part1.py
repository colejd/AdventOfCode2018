
def get_solution():
    total = 0

    with open("input.txt") as fp:
        for line in fp:
            total += eval(line)

    return total


print(get_solution())
