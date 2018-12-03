
def get_solution():
    total = 0

    with open("input.txt") as fp:
        for line in fp:
            total += eval(line)

    return "{0}".format(total)


print(get_solution())
