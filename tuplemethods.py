# Tuple with some repeated elements
t1 = (1, 2, 3, 7, 92, 12, 3, 3, 3)

# Count the number of times 3 appears in the tuple
print(t1.count(3))  # Output: 4 (3 appears 4 times in the tuple)

# Find the index of the first occurrence of the value 3
print(t1.index(3))  # Output: 2 (the first occurrence of 3 is at index 2)

# Find the index of the first occurrence of the value 3 starting from index 3
print(t1.index(3, 3))  # Output: 6 (the next occurrence of 3 after index 3 is at index 6)

# Slice the tuple to get elements from index 2 to index 5 (excluding index 5)
print(t1[2:5])  # Output: (3, 7, 92) (elements at indices 2, 3, and 4)

# Sorted version of the tuple (since tuples are immutable, sorted() returns a list)
print(sorted(t1))  # Output: [1, 2, 3, 3, 3, 3, 7, 12, 92] (sorted in ascending order)
