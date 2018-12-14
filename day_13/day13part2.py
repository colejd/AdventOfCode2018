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

    def __init__(self, position, heading, name):
        self.name = name
        self.position = position
        self.heading = heading
        self.next_turn = 0

    def __repr__(self):
        return "<id: {0} pos: {1} heading: {2}>".format(self.name, self.position, Cart.direction_lookup[self.heading])

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
            msg = "Cart {0} moved {1} to {2}. ".format(self.name, Cart.direction_lookup[old_heading], self.position)
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


def tick(carts, field):
    p = defaultdict(set)
    to_remove = []

    # Store all cart positions
    for cart in carts:
        p[cart.position].add(cart)

    # Move each cart
    for cart in sorted(carts, key=lambda item: (item.position[1], item.position[0])):
        # Ignore the cart if it's been hit in this tick by another cart
        if cart in to_remove:
            continue
        next_pos = cart.next_position

        # If the target position is another cart's position, there will be a collision.
        char_ahead = field[next_pos[1]][next_pos[0]]
        dest_cart_set = p[next_pos].copy()
        if len(dest_cart_set) >= 1:
            # Remove both carts
            p[cart.position].remove(cart)
            for c in dest_cart_set:
                p[c.position].remove(c)
            # Schedule for removal from cart set at end of tick
            to_remove += [cart] + list(dest_cart_set)
            continue

        p[cart.position].remove(cart)
        p[next_pos].add(cart)
        cart.move(char_ahead)

    if len(to_remove) > 0:
        print(to_remove)

    for cart in to_remove:
        carts.remove(cart)


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
    cart_name_index = 1
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "<":
                carts.append(Cart((x, y), Cart.LEFT, cart_name_index))
                cart_name_index += 1
                field[y][x] = "-"
            elif char == ">":
                carts.append(Cart((x, y), Cart.RIGHT, cart_name_index))
                cart_name_index += 1
                field[y][x] = "-"
            elif char == "^":
                carts.append(Cart((x, y), Cart.UP, cart_name_index))
                cart_name_index += 1
                field[y][x] = "|"
            elif char == "v":
                carts.append(Cart((x, y), Cart.DOWN, cart_name_index))
                cart_name_index += 1
                field[y][x] = "|"

    print("Carts:", carts)
    print("--------------------")

    for i in range(100000):
        tick(carts, field)
        if debug:
            print_field(field, carts)
        if len(carts) == 1:
            print("Only one cart remains!")
            return carts[0].position


print(get_solution())
