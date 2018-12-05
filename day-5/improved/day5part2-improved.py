import string

def get_input():
    with open("input.txt", "r") as myfile:
        return myfile.read().replace('\n', '')


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


def get_solution():
    line = list(get_input())

    return min(map(lambda polymer: do_pass(line, deleted_polymer=polymer), string.ascii_lowercase))


print(get_solution())
