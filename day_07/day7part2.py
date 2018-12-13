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
    for line in input_lines("input.txt"):
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

    time_taken = 0
    num_workers = 5
    worker_times = [0, 0, 0, 0, 0]
    worker_jobs = [None, None, None, None, None]

    def is_satisfied(item):
        return all(i in solution for i in prereqs[item])

    def time_for(item):
        return 61 + (ord(item.lower()) - 97)

    print(time_for("A"))

    while len(frontier) > 0:
        print("------------------")
        print("Time is now {0}".format(time_taken))
        print("Solution is currently \"{0}\"".format(solution))
        print("Frontier is currently: {0}".format(frontier))
        print("...")

        # Assign a worker to the first available job in the frontier
        # If no workers are left, wait for the next worker to free up

        # Finish any jobs that are done
        print("Finishing any completed jobs...")
        for i in range(num_workers):
            if worker_jobs[i] and worker_times[i] == 0:
                finished_job = worker_jobs[i]
                print("Finished job {0} for worker {1}.".format(finished_job, i))
                solution += finished_job
                print("  Solution is now \"{0}\"".format(solution))
                frontier.remove(finished_job)

                for item in steps[finished_job]:
                    frontier.add(item)
                worker_jobs[i] = None

        # Refresh the list of available jobs (in reverse order so that pop gives us the best available job)
        available_jobs = sorted([item for item in frontier if is_satisfied(item) and item not in worker_jobs],
                                reverse=True)
        print("Available jobs: {0}".format(available_jobs))

        # Assign new jobs to free workers
        for i in range(num_workers):
            if worker_jobs[i] is None:
                # Take the job
                if len(available_jobs) == 0:
                    continue
                candidate = available_jobs.pop()
                if candidate in worker_jobs:
                    continue
                print("Worker {0} has taken job {1}.".format(i, candidate))
                print("  Available jobs are now: {0}".format(available_jobs))
                worker_jobs[i] = candidate
                worker_times[i] = time_for(candidate)
                print("  Worker will be occupied for {0} seconds.".format(worker_times[i]))

        # At this point, we have to wait for the next worker to free up. Simulate time passed until that point.
        min_job_time = min([t for t in worker_times if t != 0], default=0)
        print("All available jobs are now taken.")
        print("  Times: {0}".format(worker_times))
        print("  Jobs:  {0}".format(worker_jobs))
        print("Waiting for {0} seconds...".format(min_job_time))
        time_taken += min_job_time
        worker_times = [max(t - min_job_time, 0) for t in worker_times]

    return solution, time_taken


print("Solution is {0} and took {1} seconds to accomplish".format(*get_solution()))
