class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect:
    def __init__(self, line):
        items = line.split()

        self.id = int(items[0].replace("#", ""))
        x, y = [int(n) for n in items[2].replace(":", "").split(",")]
        self.origin = Point(x, y)
        self.width, self.height = [int(n) for n in items[3].split("x")]

    def __str__(self):
        return "({0}, {1}) (w: {2}, h: {3})".format(self.origin.x, self.origin.y, self.width, self.height)

    @property
    def min(self):
        return self.origin

    @property
    def max(self):
        point = self.origin
        point.x += self.width
        point.y += self.height
        return point

    def overlaps(self, rect):
        if self.min.x > rect.max.x or rect.min.x > self.max.x:
            return False
        if self.min.y > rect.max.y or rect.min.y > self.max.y:
            return False
        return True

    def apply_to(self, cloth_map):
        for x in range(self.width):
            for y in range(self.height):
                cloth_map[self.origin.y + y][self.origin.x + x] += 1


def get_lines():
    with open("input.txt") as fp:
        return [line[:-1] for line in fp]


def print_map(cloth_map):
    # final_str = ""
    for y in range(len(cloth_map)):
        # line = ""
        print(cloth_map[y])
        # for x in range(len(cloth_map[0])):
        #     if cloth_map[y][x] == 0:
        #         line += "."
        #     else:
        #         line += "X"
        #
        # final_str += line + "\n"

    # print(final_str)


def get_solution():
    map_size = 1000
    cloth_map = [[0 for i in range(map_size)] for j in range(map_size)]

    rects = [Rect(line) for line in get_lines()]
    for rect in rects:
        rect.apply_to(cloth_map)

    print_map(cloth_map)

    overlapping = 0
    for y in range(len(cloth_map)):
        for x in range(len(cloth_map[0])):
            if cloth_map[y][x] >= 2:
                overlapping += 1

    return overlapping


print(get_solution())
