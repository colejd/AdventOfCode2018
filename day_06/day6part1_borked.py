from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from collections import defaultdict
from collections import Counter
import string
import time

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

from scipy.spatial import cKDTree

def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

def get_bounds(points):
    x_max = 0
    y_max = 0
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

    return (x_min, x_max, y_min, y_max)

@timeit
def get_solution():
    input_strings = input_lines("test_input.txt")
    data = list(map(lambda line: [int(n) for n in line.split(", ")], input_strings))
    points = np.array(data)
    vor = Voronoi(points)

    # print(vor.regions)
    # print(vor.vertices)
    # print(vor.point_region)

    # for each item in vor.regions
    # if the region is finite
    # get the corresponding point from vor.point_region
    # and associate it with points

    largest_area = 0
    largest_area_index = -1

    for i in range(len(vor.regions)):
        if i == 0:
            continue

        # print(np.where(vor.point_region == i)[0][0])

        region = vor.regions[i]
        if -1 in region:
            # Region is not finite
            continue

        # Region with point indexed at `i` is finite
        # Compute area
        verts = [vor.vertices[n] for n in region]
        area = PolygonArea(verts)
        # print(verts)
        # print(area)

        if area > largest_area:
            largest_area = area
            # largest_area_index = i
            largest_area_index = np.where(vor.point_region == i)[0][0]

    print("Largest finite region comes from point {0} and has an area of {1}".format(largest_area_index, largest_area))

    bounds = get_bounds(points)
    sampling_points = []

    points_str = ""
    for y in range(bounds[2] - 1, bounds[3] + 1):
        line_str = ""
        for x in range(bounds[0] - 1, bounds[1] + 1):
            line_str += "({0}, {1})".format(x + 0.5, y + 0.5)
            sampling_points.append([x + 0.5, y + 0.5])
        points_str += line_str + "\n"
    print("Bounds: {0}".format(bounds))
    print("Sampling Points:\n{0}".format(points_str))

    voronoi_kdtree = cKDTree(points)
    test_point_dist, test_point_regions = voronoi_kdtree.query(sampling_points)
    f = list(map(lambda x: string.ascii_uppercase[x], test_point_regions))
    print(Counter(f).most_common(26))
    print(f)

    # for y in range(bounds[2] - 1, bounds[3] + 1):
    #     for x in range(bounds[0] - 1, bounds[1] + 1):
    #         pass

    # print(Counter(test_point_regions))
    # print(Counter(test_point_regions).most_common(1))

    print("Sampled area of largest finite poly is {0}".format(test_point_regions[largest_area_index + 1]))

    voronoi_plot_2d(vor)
    plt.show()


print(get_solution())
