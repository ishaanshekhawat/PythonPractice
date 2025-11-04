# Write a function fizz_buzz_sum to find the sum of all multiples of 3 or 5 below a target value.
# For example, if the target value was 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9.
# Because 3+5+6+9=23, our function would return 23.

from functools import reduce  # Import reduce to sum up list elements

# Function to calculate the sum of all multiples of 3 or 5 below a target value
def fizz_buzz_sum(target):
    # Create two empty lists to store multiples of 3 and 5 separately
    mult3 = []
    mult5 = []

    # Loop through all numbers starting from 2 up to (but not including) the target value
    for i in range(2, target):
        # Check if the number is divisible by 3
        if i % 3 == 0:
            mult3.append(i)  # Add to list of multiples of 3
        # If not divisible by 3 but divisible by 5
        elif i % 5 == 0:
            mult5.append(i)  # Add to list of multiples of 5
    
    # Combine both lists and sum all numbers using reduce
    # reduce(lambda x, y: x + y, list) adds all elements in the list together
    return reduce(lambda x, y: x + y, (mult3 + mult5))
