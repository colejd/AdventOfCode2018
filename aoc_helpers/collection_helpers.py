def key_for_largest_value(dictionary, key=None):
    if not key:
        key = dictionary.get
    return max(dictionary, key=key)


def pair_for_largest_value(dictionary, key=None):
    if not key:
        key = dictionary.get
    k = key_for_largest_value(dictionary, key=key)
    return k, dictionary[k]


def key_for_smallest_value(dictionary, key=None):
    if not key:
        key = dictionary.get
    return min(dictionary, key=key)


def pair_for_smallest_value(dictionary, key=None):
    if not key:
        key = dictionary.get
    k = key_for_smallest_value(dictionary, key=key)
    return k, dictionary[k]


def range_inclusive(low, high):
    return range(low, high + 1)

