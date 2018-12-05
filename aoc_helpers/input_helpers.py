def input_string(filename="input.txt"):
    with open(filename, "r") as fp:
        return fp.read().replace('\n', '')


def input_lines(filename="input.txt"):
    return list(open(filename))
