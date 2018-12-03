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

        self.overlapped = False

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

    def apply_to(self, cloth_map, rects):
        for x in range(self.width):
            for y in range(self.height):
                occupying_ids = cloth_map[self.origin.y + y][self.origin.x + x]

                # If the cell we're marking is going to overlap any others,
                # mark this rect and the other occupying rects as overlapping
                if len(occupying_ids) != 0:
                    self.overlapped = True
                    for other_id in occupying_ids:
                        rects[other_id].overlapped = True

                cloth_map[self.origin.y + y][self.origin.x + x].append(self.id)


def get_lines():
    with open("input.txt") as fp:
        return [line[:-1] for line in fp]


def get_solution():
    map_size = 1000
    cloth_map = [[[] for i in range(map_size)] for j in range(map_size)]

    rects = {}
    for rect in [Rect(line) for line in get_lines()]:
        rects[rect.id] = rect
        rect.apply_to(cloth_map, rects)

    for rect in list(rects.values()):
        if not rect.overlapped:
            return rect.id


print(get_solution())
