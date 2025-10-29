# Initial set with some repeated elements (sets automatically remove duplicates)
s1 = {1, 2, 3, 7, 92, 12, 3, 3, 3}
print(s1)  # Output: {1, 2, 3, 7, 92, 12} (duplicates are removed automatically)

# Add a new element 8 to the set
s1.add(8)
print(s1)  # Output: {1, 2, 3, 7, 8, 92, 12} (8 is added)

# Attempt to remove an element that is not in the set (will raise KeyError if uncommented)
# s1.remove(4843)

# Using discard() to remove an element from the set. If the element doesn't exist, it doesn't raise an error.
s1.discard(4843)  # No error even though 4843 is not in the set
print(s1)  # Output: {1, 2, 3, 7, 8, 92, 12} (4843 was not in the set, so nothing happens)

# Pop a random element from the set. Since sets are unordered, we can't predict which one will be removed.
print(s1.pop())  # Output: Random element (e.g., 1)
print(s1)  # Output: The set after popping one random element

# Second set for set operations
s2 = {2, 34, 6, 2, 6, 3, 1, 7}
print(s2)  # Output: {1, 2, 3, 6, 7, 34} (duplicates are removed automatically)

# Union of s1 and s2: combines elements from both sets, removing duplicates
print(s1.union(s2))  # Output: Set of all unique elements from s1 and s2
print(s1 | s2)  # Another way to get the union, using the '|' operator

# Intersection of s1 and s2: elements that are present in both sets
print(s1.intersection(s2))  # Output: {1, 2, 3, 7} (common elements in both sets)
print(s1 & s2)  # Another way to get the intersection, using the '&' operator

# Difference of s1 and s2: elements that are in s1 but not in s2
print(s1.difference(s2))  # Output: elements in s1 but not in s2
print(s1 - s2)  # Another way to get the difference, using the '-' operator

# Symmetric difference of s1 and s2: elements that are in either s1 or s2, but not both
print(s1.symmetric_difference(s2))  # Output: elements in s1 or s2, but not both
print(s1 ^ s2)  # Another way to get the symmetric difference, using the '^' operator

# Sorted version of s1: converts the set to a sorted list
print(sorted(s1))  # Output: A sorted list of the elements in s1
