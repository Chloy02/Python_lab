
def merging_Dict(*args):
    """
    Merges multiple dictionaries into one.
    If a key appears in more than one dictionary, the value from the last dictionary is used.
    """
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict

def find_common_keys(*args):
    """
    Finds common keys across multiple dictionaries.
    """
    if not args:
        return set()  # Return an empty set if no dictionaries are provided
    
    # Start with the keys of the first dictionary
    common_keys = set(args[0].keys())
    
    # Intersect with keys of remaining dictionaries
    for dictionary in args[1:]:
        common_keys &= dictionary.keys()
        
    return common_keys
