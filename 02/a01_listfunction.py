
def find_max(lst):
    """Returns the maximum value in the list."""
    return max(lst)

def find_min(lst):
    """Returns the minimum value in the list."""
    return min(lst)

def sum_list(lst):
    """Returns the sum of all elements in the list."""
    return sum(lst)

def average_list(lst):
    """Returns the average of the list."""
    return sum(lst) / len(lst)

def median_list(lst):
    """Returns the median of the list."""
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    
    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
    
    return median
