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

    earliest_step = None
    steps = defaultdict(set)
    prereqs = defaultdict(set)

    # Construct the sequence of steps
    for line in input_lines():
        spl = line.split()
        prereq_id = spl[1]
        step_id = spl[7]

        if not earliest_step:
            earliest_step = prereq_id

        steps[prereq_id].add(step_id)
        prereqs[step_id].add(prereq_id)

    pprint(steps)
    pprint(prereqs)

    solution = ""

    # The root nodes are the ones with no prerequisites.
    frontier = set(steps.keys()) - set(prereqs.keys())
    print("Root nodes: {0}".format(frontier))

    def is_satisfied(item):
        return all(i in solution for i in prereqs[item])

    while len(frontier) > 0:
        print("------------------")
        print("Solution is currently \"{0}\"".format(solution))
        print("Frontier: {0}".format(frontier))

        # The next step is the first one in the sorted frontier that has its prerequisites satisfied
        filtered_frontier = [item for item in frontier if is_satisfied(item)]

        next_step = sorted(filtered_frontier)[0]
        print("Choosing step \"{0}\"".format(next_step))
        solution += next_step
        frontier.remove(next_step)

        for item in steps[next_step]:
            frontier.add(item)

    return solution


print("Solution is {0}".format(get_solution()))
