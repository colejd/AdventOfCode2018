from aoc_helpers.perf_helpers import *
from aoc_helpers.input_helpers import *
from aoc_helpers.collection_helpers import *

from collections import defaultdict
from collections import Counter
import string
import time
from pprint import pprint


class Node:

    def __init__(self, data, identifier=1):
        self.data = data
        self.num_child_nodes = int(data[0])
        self.num_metadata_entries = int(data[1])

        self.child_nodes = []

        print("Creating node {0}".format(identifier))

        # All nodes are at least 3 long (header = 2 and at least 1 metadata entry)
        self.length = 2 + self.num_metadata_entries

        self.child_index = 2
        for i in range(self.num_child_nodes):
            # Create child nodes and offset by their metadata_index
            new_data = data[self.child_index:-self.num_metadata_entries]
            new_node = Node(new_data, identifier=identifier+i+1)
            self.child_nodes.append(new_node)
            self.child_index += new_node.length
            self.length += new_node.length

        # Always the last `num_metadata_entries` elements
        # print(data)
        # print("{0} metadata entries starting at index {1}".format(self.num_metadata_entries, self.child_index))
        self.metadata_entries = data[self.child_index: self.child_index + self.num_metadata_entries]
        # print(self.metadata_entries)

    def __str__(self):
        out = "{0} {1} ".format(self.num_child_nodes, self.num_metadata_entries)
        for child in self.child_nodes:
            out += str(child)

        for entry in self.metadata_entries:
            out += "{0} ".format(entry)

        return out

    # Each item is the sum of its metadata + the sum of the metadata for each direct child
    def meta_sum(self):
        # Base case: No child nodes. Return sum of metadata.
        n = sum([int(item) for item in self.metadata_entries])
        for child in self.child_nodes:
            n += child.meta_sum()
        return n

    def value_sum(self):
        meta = [int(item) for item in self.metadata_entries]
        if self.num_child_nodes == 0:
            return sum(meta)

        return sum([self.child_nodes[i - 1].value_sum() for i in meta if 1 <= i <= self.num_child_nodes])


@timeit
def get_solution():
    data = input_string().split(" ")

    print(data)
    root = Node(data)
    print(root.value_sum())


print(get_solution())
