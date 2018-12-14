from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *
from aoc_helpers.misc_helpers import *

from collections import defaultdict
from collections import Counter
import string
import time
from pprint import pprint

import sys
import time
from builtins import print

# from curses import wrapper


debug = False

if debug:
    print = log


class Cart:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    direction_lookup = {
        (-1, 0): "LEFT",
        (1, 0): "RIGHT",
        (0, -1): "UP",
        (0, 1): "DOWN"
    }

    def __init__(self, position, heading):
        self.position = position
        self.heading = heading
        self.next_turn = 0

    def __repr__(self):
        return "<pos: {0} heading: {1}>".format(self.position, Cart.direction_lookup[self.heading])

    @property
    def left_heading(self):
        if self.heading == Cart.UP:
            return -1, 0
        if self.heading == Cart.DOWN:
            return 1, 0
        if self.heading == Cart.LEFT:
            return 0, 1
        if self.heading == Cart.RIGHT:
            return 0, -1
        return None

    @property
    def right_heading(self):
        if self.heading == Cart.UP:
            return 1, 0
        if self.heading == Cart.DOWN:
            return -1, 0
        if self.heading == Cart.LEFT:
            return 0, -1
        if self.heading == Cart.RIGHT:
            return 0, 1
        return None

    def move(self, char):
        """
        Move the cart based on its heading, then adjust the heading based on the char moved to.
        """
        self.position = self.next_position

        old_heading = self.heading

        if char == "\\":
            if self.heading == Cart.DOWN or self.heading == Cart.UP:
                self.heading = self.left_heading
            else:
                self.heading = self.right_heading
        elif char == "/":
            if self.heading == Cart.DOWN or self.heading == Cart.UP:
                self.heading = self.right_heading
            else:
                self.heading = self.left_heading
        elif char == "+":
            if self.next_turn == 0:
                self.heading = self.left_heading
                self.next_turn = 1
            elif self.next_turn == 1:
                # Don't alter heading (go straight)
                self.next_turn = 2
            elif self.next_turn == 2:
                self.heading = self.right_heading
                self.next_turn = 0

        if debug:
            msg = "Cart moved {0} to {1}. ".format(Cart.direction_lookup[old_heading], self.position)
            if old_heading != self.heading:
                msg += "Heading is now {0}".format(Cart.direction_lookup[self.heading])
            print(msg)

    @property
    def next_position(self):
        return self.position[0] + self.heading[0], self.position[1] + self.heading[1]

    def as_char(self):
        if self.heading == Cart.DOWN:
            return "v"
        if self.heading == Cart.UP:
            return "^"
        if self.heading == Cart.LEFT:
            return "<"
        if self.heading == Cart.RIGHT:
            return ">"


def print_field(field, carts):
    field_copy = [line.copy() for line in field.copy()]

    for cart in carts:
        x, y = cart.position
        field_copy[y][x] = cart.as_char()

    for line in field_copy:
        print("".join(line))

    # ln = 0
    #
    # for line in field_copy:
    #     sys.stdout.write("".join(line) + "\n")
    #     ln += len(line) + 1
    #
    # sys.stdout.write('\b' * ln)
    # sys.stdout.flush()
    # time.sleep(0.1)


def tick(carts, field):
    p = defaultdict(int)

    # Store all cart positions
    for cart in carts:
        p[cart.position] += 1

    # Move each cart
    for cart in sorted(carts, key=lambda item: (item.position[1], item.position[0])):
        next_pos = cart.next_position

        # If the target position is another cart's position, there will be a collision.
        char_ahead = field[next_pos[1]][next_pos[0]]
        if p[next_pos] >= 1:
            return next_pos

        p[cart.position] -= 1
        p[next_pos] += 1
        cart.move(char_ahead)


@timeit
def get_solution():
    data = [list(item) for item in input_lines("input.txt")]

    field = [line.copy() for line in data.copy()]

    print("Starting state:")
    for line in field:
        print("".join(line))

    carts = []

    # Find all the carts and their headings, replacing the carts with track as we go.
    # After this, the field is used purely for looking up track information when moving
    # the carts.
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "<":
                carts.append(Cart((x, y), Cart.LEFT))
                field[y][x] = "-"
            elif char == ">":
                carts.append(Cart((x, y), Cart.RIGHT))
                field[y][x] = "-"
            elif char == "^":
                carts.append(Cart((x, y), Cart.UP))
                field[y][x] = "|"
            elif char == "v":
                carts.append(Cart((x, y), Cart.DOWN))
                field[y][x] = "|"

    print("Carts:", carts)
    print("--------------------")

    for i in range(500):
        collision = tick(carts, field)
        if debug:
            print_field(field, carts)
        if collision is not None:
            print(i)
            return collision


print(get_solution())


# def main(stdscr):
#     # Clear screen
#     stdscr.clear()
#
#     # This raises ZeroDivisionError when i == 10.
#     for i in range(0, 11):
#         v = i - 10
#         stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10 / v))
#
#     stdscr.refresh()
#     stdscr.getkey()
#
# wrapper(main)
