
def add_element(s, elem):
    """Adds an element to the set."""
    s.add(elem)
    return s

def remove_element(s, elem):
    """Removes an element from the set if it exists."""
    s.discard(elem)  # discard does not raise an error if elem is not found
    return s

def union_and_intersection(s1, s2):
    """Returns the union and intersection of two sets."""
    union_set = s1 | s2
    intersection_set = s1 & s2
    return union_set, intersection_set

def difference(s1, s2):
    """Returns the difference S1 - S2."""
    return s1 - s2

def is_subset(s1, s2):
    """Checks if S1 is a subset of S2."""
    return s1 <= s2

def set_length(s):
    """Returns the length of the set without using len()."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    """Returns the symmetric difference of two sets."""
    return s1 ^ s2

def power_set(s):
    """Returns the power set of the given set."""
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def unique_subsets(s):
    """Returns all unique subsets of the given set."""
    return power_set(s)
