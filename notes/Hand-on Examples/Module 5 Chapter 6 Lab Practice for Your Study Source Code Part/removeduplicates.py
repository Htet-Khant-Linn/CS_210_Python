# Remove Duplicates from a List 
# Write a function remove_duplicates(lst) that removes duplicate elements from a list and returns a new list.

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

"""
Example usage:
remove_duplicates([5,5,4,6,7])
"""
