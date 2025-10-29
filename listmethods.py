# Initial list with some repeated numbers
l1 = [1, 2, 3, 7, 92, 12, 3, 3, 3]

# Append the value 4 to the end of the list
l1.append(4)
print(l1)  # Output: [1, 2, 3, 7, 92, 12, 3, 3, 3, 4]

# Extend the list by adding elements from another list [3, 2, 2]
l1.extend([3, 2, 2])
print(l1)  # Output: [1, 2, 3, 7, 92, 12, 3, 3, 3, 4, 3, 2, 2]

# Extend the list again, this time using a tuple (3, 2, 2)
l1.extend((3, 2, 2))
print(l1)  # Output: [1, 2, 3, 7, 92, 12, 3, 3, 3, 4, 3, 2, 2, 3, 2, 2]

# Find the index of the first occurrence of the value 3 starting from index 9
print(l1.index(3, 9))  # Output: 10 (first 3 after index 9 is at index 10)

# Insert the value 5 at index 10, shifting other elements to the right
l1.insert(10, 5)
print(l1)  # Output: [1, 2, 3, 7, 92, 12, 3, 3, 3, 4, 5, 3, 2, 2, 3, 2, 2]

# Pop (remove and return) the element at the third-to-last position (index -3)
l1.pop(-3)
print(l1)  # Output: [1, 2, 3, 7, 92, 12, 3, 3, 3, 4, 5, 3, 2, 2, 3, 2]

# Count the number of occurrences of the value 2 in the list
print(l1.count(2))  # Output: 3 (there are 3 occurrences of 2)

# Remove the first occurrence of the value 2 from the list
l1.remove(2)
print(l1)  # Output: [1, 3, 7, 92, 12, 3, 3, 3, 4, 5, 3, 2, 2, 3, 2]

# Sort the list in ascending order
l1.sort()
print(l1)  # Output: [1, 3, 3, 3, 3, 4, 5, 7, 12, 2, 2, 2, 3, 92]

# Reverse the order of the list
l1.reverse()
print(l1)  # Output: [92, 3, 2, 2, 2, 3, 12, 7, 5, 4, 3, 3, 3, 1]
