# Initial dictionary with integer keys
d1 = {1: "apple", 2: "banana", 3: "cherry", 4: "date"}

# Print the original dictionary
print(d1)

# Using .get() method to retrieve value for key 3 (existing key)
print(d1.get(3))

# Using .get() method to retrieve value for key 5 (non-existing key, returns None)
print(d1.get(5))

# .keys() method returns all the keys in the dictionary
print(d1.keys())

# .values() method returns all the values in the dictionary
print(d1.values())

# .items() method returns a view object displaying a list of key-value tuple pairs
print(d1.items())

# Iterating through dictionary using .items() to print both keys and values
for k, v in d1.items():
    print(f'Key is {k} and Value is {v}')

# Another dictionary to be combined with d1
d2 = {5: 'fig', 6: 'grape', 7: 'honeydew'}

# Empty dictionary where d2 will be merged
d3 = {}

# Using update() to merge d2 into d3
d3.update(d2)

# Print the updated dictionary d3 (contains d2's key-value pairs)
print(d3)

# Using pop() to remove and return the value of key 6 from d3
print(d3.pop(6))

# Print d3 after popping key 6
print(d3)

# Using popitem() to remove and return an arbitrary key-value pair from d3
print(d3)

# Print d3 after popping an arbitrary key-value pair
print(d3)

# Using fromkeys() to create a new dictionary with keys [5, 6, 7] and default value None
d3.fromkeys([5,6,7])

# Print d3 after using fromkeys (it does not modify d3 in-place)
print(d3)
