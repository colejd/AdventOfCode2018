import string

letters = list(string.ascii_lowercase)

def get_input():
    with open("input.txt", "r") as myfile:
        return myfile.read().replace('\n', '')


def do_pass(line):
    lastchar = line[0]
    remove = []
    skip_next = False
    for index, char in enumerate(line[1:]):
        if skip_next:
            skip_next = False
            lastchar = char
            continue
        if char.lower() == lastchar.lower():
            if (char.isupper() and not lastchar.isupper()) or (not char.isupper() and lastchar.isupper()):
                remove.append(index)
                remove.append(index + 1)
                if index+1 < len(line) and line[index+1].lower() == char.lower():
                    skip_next = True
        lastchar = char

    # print(remove)
    if len(remove) == 0:
        return None

    # Remove all characters at the given indices
    return [v for i, v in enumerate(line) if i not in remove]

def get_reaction(line):
    while True:
        result = do_pass(line)
        if result == None:
            break
        else:
            line = result

    return line

def get_solution():
    line = get_input()
    smallest = 10000000000
    for char in list(string.ascii_lowercase):
        print("Doing reduction for \"{0}\"".format(char))
        line_variant = line.replace(char, "").replace(char.upper(), "")
        reacted = get_reaction(line_variant)
        print("Length is {0}".format(len(reacted)))
        if len(reacted) < smallest:
            smallest = len(reacted)
            print("New smallest")
    return smallest

print(get_solution())
