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


@timeit
def get_solution(num_players, last_marble_value):
    marbles = [0]
    current_marble = 0
    scores = [0 for _ in range(num_players)]
    current_player = 0

    for i in range_inclusive(1, last_marble_value):

        if i % 23 == 0:
            scores[current_player] += i
            other_marble_index = (current_marble - 7 + len(marbles)) % len(marbles)
            scores[current_player] += marbles.pop(other_marble_index)
            current_marble = other_marble_index
        else:
            current_marble = ((current_marble + 1) % len(marbles)) + 1
            marbles.insert(current_marble, i)

        current_player = (current_player + 1) % num_players

    return max(scores)


test(get_solution(9, 25), 32)
test(get_solution(10, 1618), 8317)
test(get_solution(13, 7999), 146373)
test(get_solution(17, 1104), 2764)
test(get_solution(21, 6111), 54718)
test(get_solution(30, 5807), 37305)

print(get_solution(428, 70825))
