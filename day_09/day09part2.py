from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *
from aoc_helpers.test_helpers import *

from collections import defaultdict
from collections import Counter
import string
import time
from pprint import pprint

from itertools import cycle


class Marble:
    def __init__(self, value):
        self.value = value

        self.next_marble = self
        self.prev_marble = self


@timeit
def get_solution(num_players, last_marble_value):
    current_marble = Marble(0)
    head_marble = current_marble
    scores = [0 for _ in range(num_players)]
    current_player = 0

    for i in range_inclusive(1, last_marble_value):

        # pr = []
        # pr_marble = head_marble
        # for idx in range(i):
        #     pr.append(pr_marble.value)
        #     pr_marble = pr_marble.next_marble
        # print("Value: {0}".format(pr))
        #
        # link = []
        # pr_marble = head_marble
        # for idx in range(i):
        #     pr_marble = pr_marble.next_marble
        #     link.append(pr_marble.next_marble.value)
        # print("Links: {0}".format(link))

        if i % 23 == 0:
            scores[current_player] += i
            seven_prev = current_marble.prev_marble.prev_marble.prev_marble.prev_marble.prev_marble.prev_marble.prev_marble
            scores[current_player] += seven_prev.value
            seven_prev.prev_marble.next_marble = seven_prev.next_marble
            seven_prev.next_marble.prev_marble = seven_prev.prev_marble
            current_marble = seven_prev.next_marble
        else:
            m1 = current_marble.next_marble
            m2 = current_marble.next_marble.next_marble

            new_marble = Marble(i)

            new_marble.next_marble = m2
            m2.prev_marble = new_marble

            new_marble.prev_marble = m1
            m1.next_marble = new_marble

            current_marble = new_marble

        current_player = (current_player + 1) % num_players

    return max(scores)


test(get_solution(9, 25), 32)
test(get_solution(10, 1618), 8317)
test(get_solution(13, 7999), 146373)
test(get_solution(17, 1104), 2764)
test(get_solution(21, 6111), 54718)
test(get_solution(30, 5807), 37305)

test(get_solution(428, 70825), 398502)

print(get_solution(428, 7082500))
