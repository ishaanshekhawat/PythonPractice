# Write a function to get the intersection of two lists.
# Example:
# A = [1, 2, 3, 4, 5]
# B = [0, 1, 3, 7]
# Output → [1, 3]

def intersection(a, b):
    # Initialize an empty set to store the common elements.
    # A set is used because it automatically avoids duplicates.
    inter1 = set()
    
    # Loop through each element in list 'a'
    for i in a:
        # Check if the element from 'a' also exists in list 'b'
        if i in b:
            # If it does, add it to the set of intersections
            inter1.add(i)
    
    # Convert the set back to a list before returning
    # (since the expected output is a list, not a set)
    return list(inter1)


# Example usage: should print [1, 3]
print(intersection([1, 2, 3, 4, 5], [0, 1, 3, 7]))
