from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *
from collections import Counter
from collections import defaultdict
import string
from pprint import pprint


def get_bounds(points):
    x_max = -1000000000000
    y_max = -1000000000000
    x_min = 1000000000000
    y_min = 1000000000000
    for point in points:
        if point[0] < x_min:
            x_min = point[0]
        if point[0] > x_max:
            x_max = point[0]
        if point[1] < y_min:
            y_min = point[1]
        if point[1] > y_max:
            y_max = point[1]

    return x_min, x_max, y_min, y_max


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Is the point along the edge of the bounds? If so, the region it belongs to is infinite.
def is_edge(point, bounds):
    return point[0] == bounds[0] or point[0] == bounds[1] \
        or point[1] == bounds[2] or point[1] == bounds[3]


def visualize(region_points, region_indices_for_points, bounds):
    output_str = ""
    for y in range_inclusive(bounds[2], bounds[3]):
        line_str = ""
        for x in range_inclusive(bounds[0], bounds[1]):
            point = (x, y)
            item = region_indices_for_points[point]
            if item is not None:
                line_str += string.ascii_uppercase[item] if point in region_points else string.ascii_lowercase[item]
            else:
                line_str += "."
        output_str += line_str + "\n"
    print(output_str)


@timeit
def get_solution():
    input_strings = input_lines()
    region_points = list(map(lambda line: tuple([int(n) for n in line.split(", ")]), input_strings))
    bounds = get_bounds(region_points)

    print("Bounds: {0}".format(bounds))

    points_for_region_index = defaultdict(list)
    region_indices_for_points = {}
    infinite_point_indices = set()

    # TODO: If the region point is along the edge, we can remove it for an optimization

    for y in range_inclusive(bounds[2], bounds[3]):
        for x in range_inclusive(bounds[0], bounds[1]):
            current_point = (x, y)

            # Get the distance of all input points from this point
            df = {i: manhattan_distance(v, current_point) for (i, v) in enumerate(region_points)}
            # Get the input point with the smallest distance from this point
            min_index, min_val = pair_for_smallest_value(df)

            # If there is more than one point with the shortest distance, discard this point
            if list(df.values()).count(min_val) >= 2:
                region_indices_for_points[current_point] = None
                continue

            points_for_region_index[min_index].append(current_point)
            region_indices_for_points[current_point] = min_index
            if is_edge(current_point, bounds):
                infinite_point_indices.add(min_index)

    # Print the area for each point index
    # pprint({k: len(v) for (k, v) in nearest_point_index_lookup.items()})

    # Get the k:v pairs for only those points that have a finite area
    filtered = {k: len(v) for (k, v) in points_for_region_index.items() if k not in infinite_point_indices}
    largest_finite_area_index, largest_finite_area = pair_for_largest_value(filtered)

    print("Largest finite region is: {0} with an area of {1}".format(
        largest_finite_area_index,
        largest_finite_area
    ))

    return largest_finite_area


print(get_solution())

# Answer is 3660
