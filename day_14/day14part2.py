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
def get_solution(pattern):
    recipes = "37"

    a = 0
    b = 1

    while pattern not in recipes[-(len(pattern) + 1):]:
        recipes += str(int(recipes[a]) + int(recipes[b]))

        if debug:
            print(recipes)

        a = (a + int(recipes[a]) + 1) % len(recipes)
        b = (b + int(recipes[b]) + 1) % len(recipes)

    return recipes.index(pattern)


assert get_solution("51589") == 9
assert get_solution("01245") == 5
assert get_solution("92510") == 18
assert get_solution("59414") == 2018

assert get_solution("607331") == 20258123

print(get_solution("084601"))
