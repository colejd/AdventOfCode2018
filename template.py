from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *

from collections import defaultdict
from collections import Counter
import string
import time
from pprint import pprint


@timeit
def get_solution():
    data = input_lines()


print(get_solution())
