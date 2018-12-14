from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *
from aoc_helpers.misc_helpers import *

from collections import defaultdict
from collections import Counter
import string
import time
from pprint import pprint
from builtins import print


debug = False

if debug:
    print = log


@timeit
def get_solution(target_iterations):
    # target_iterations = 84601
    recipes = [3, 7]

    a = 0
    b = 1

    while len(recipes) < target_iterations + 10:
        new_recipes = [int(n) for n in str(recipes[a] + recipes[b])]
        recipes += new_recipes

        if debug:
            print(recipes)

        a = (a + recipes[a] + 1) % len(recipes)
        b = (b + recipes[b] + 1) % len(recipes)

    final = recipes[target_iterations:target_iterations + 10]
    return "".join([str(n) for n in final])


assert get_solution(5) == "0124515891"
assert get_solution(18) == "9251071085"
assert get_solution(2018) == "5941429882"

print(get_solution(84601))
