
def get_input():
    with open("input.txt", "r") as myfile:
        return myfile.read().replace('\n', '')


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


def get_solution():
    line = list(get_input())
    print(input)
    result = do_pass(line)
    return len(result)


print(get_solution())
