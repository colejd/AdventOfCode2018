import string


def input_string(filename="input.txt"):
    with open(filename, "r") as fp:
        return fp.read().replace('\n', '')


def input_lines(filename="input.txt"):
    with open(filename, "r") as fp:
        return fp.read().splitlines()


def asupper(i):
    return string.ascii_uppercase[i]


def aslower(i):
    return string.ascii_lowercase[i]
