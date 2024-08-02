from a02_modules import *

# Example sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Demonstrating the functions
print("Original Set1:", set1)
print("Original Set2:", set2)

# Add element
print("\nAdd element 5 to Set1:", add_element(set1, 5))

# Remove element
print("Remove element 2 from Set1:", remove_element(set1, 2))

# Union and Intersection
union_set, intersection_set = union_and_intersection(set1, set2)
print("Union of Set1 and Set2:", union_set)
print("Intersection of Set1 and Set2:", intersection_set)

# Difference
print("Difference Set1 - Set2:", difference(set1, set2))

# Is Subset
print("Is Set1 a subset of Set2?", is_subset(set1, set2))

# Set Length
print("Length of Set1:", set_length(set1))

# Symmetric Difference
print("Symmetric Difference of Set1 and Set2:", symmetric_difference(set1, set2))

# Power Set
print("Power Set of Set1:", power_set(set1))

# Unique Subsets
print("Unique Subsets of Set1:", unique_subsets(set1))
