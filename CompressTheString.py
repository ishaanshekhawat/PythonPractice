import itertools  # Importing itertools to use groupby function

# Taking user input as a string of numbers
numbers_str = input()

# Initialize an empty list to store the individual digits as integers
numbers = []

# Loop through each character in the input string
for i in numbers_str:
    numbers.append(int(i))  # Convert each character to an integer and add to the list

# Initialize an empty list to store the results
ls = []

# Use itertools.groupby to group consecutive equal elements in the numbers list
# It returns consecutive groups with the same value and the corresponding key
for key, group in itertools.groupby(numbers):
    tuplee = (len(list(group)), key)  # Create a tuple (group size, element value)
    ls.append(str(tuplee))  # Convert the tuple to string and append to the results list

# Print the result list, joining elements with a space
print(' '.join(ls))
