
def get_input():
    with open("input.txt", "r") as myfile:
        return myfile.read().replace('\n', '')

# def do_pass(line):
#     lastchar = line[0]
#     for index, char in enumerate(line[1:]):
#         if char.lower() == lastchar.lower():
#             if (char.isupper() and not lastchar.isupper()) or (not char.isupper() and lastchar.isupper()):
#                 print("Removing {0}{1}".format(lastchar, char))
#                 # print(line[:index])
#                 # print(line[index + 1:])
#                 return line[:index] + line[index + 2:]
#         lastchar = char
#     return None


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
                # print("Removing {0}{1}".format(lastchar, char))
                # print(line[:index])
                # print(line[index + 1:])
                remove.append(index)
                remove.append(index + 1)
                if index+1 < len(line) and line[index+1].lower() == char.lower():
                    skip_next = True
        lastchar = char

    print(remove)
    if len(remove) == 0:
        return None

    # Remove all characters at the given indices
    return [v for i, v in enumerate(line) if i not in remove]


def get_solution():
    line = list(get_input())
    print(input)
    while True:
        result = do_pass(line)
        print(result)
        if result == None:
            break
        else:
            line = result

    return len(line)


print(get_solution())
