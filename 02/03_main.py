
from a03_module import merging_Dict, find_common_keys

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
dict3 = {'c': 5, 'd': 6, 'e': 7}

# Merging dictionaries
merged_dict = merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged_dict)

# Finding common keys
common_keys = find_common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys)
