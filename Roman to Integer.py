# Given a valid Roman numeral, convert it to an integer.

# In case you don't think about the Roman empire that often, and need a crash-course on how to go from Superbowl "XLIV" to an actual number, '
# 'here's the table mapping the numerals to their values:

# Symbol	Value
#   I	        1
#   V	        5
#   X	        10
#   L	        50
#   C     	    100
#   D	        500
#   M	        1000

# The numerals are generally written from largest to smallest from left to right. For example, the number 11 is written as XI, where X represents 10 and I represents 1, so the total is 11.

# Similarly, XXX would be 30 (unless we're talking about your browser's search history).

# Example 1:
# Input: s = "XI"

# Output: 11

# Explanation: X = 10, I = 1, XI = 11

# In certain cases, a smaller numeral comes before a larger one to indicate subtraction. For example, 4 is written as IV, where I comes before V, meaning 1 is subtracted from 5, resulting in 4. Similarly, 90 is written as XC, where X comes before C, meaning 10 is subtracted from 100, giving 90.

# This subtraction rule applies in the following cases:

# I comes before V (5) or X (10) to make 4 and 9.
# X comes before L (50) or C (100) to make 40 and 90.
# C comes before D (500) or M (1000) to make 400 and 900.

# Example 2:
# Input: s = "LXIX"

# Output: 69

# Explanation: L = 50, X = 10, IX = 9, LXIX = 69. Nice.

from functools import reduce  # Import reduce to sum up list elements

# Function to convert a Roman numeral string into an integer
def romanToInt(s):
    ls = []  # List to store the numeric values of each Roman character
    
    # Step 1: Convert each Roman numeral character to its integer value
    for i in s:
        if i == 'I':
            ls.append(1)
        elif i == 'V':
            ls.append(5)
        elif i == 'X':
            ls.append(10)
        elif i == 'L':
            ls.append(50)
        elif i == 'C':
            ls.append(100)
        elif i == 'D':
            ls.append(500)
        elif i == 'M':
            ls.append(1000)
    
    # At this point, 'ls' contains the numeric equivalent of each Roman symbol.
    # Example: "LXIX" → [50, 10, 1, 10]
    
    ls1 = []  # This list will store the adjusted values considering subtraction rules
    
    # Step 2: Apply the subtraction rule
    # If a smaller value appears before a larger one, we subtract it.
    for i in range(len(ls) - 1):
        if ls[i] < ls[i + 1]:
            ls1.append(-ls[i])  # Subtract the smaller number
        else:
            ls1.append(ls[i])   # Otherwise, add it normally
    
    # Append the last value, since it’s always added
    ls1.append(ls[-1])
    
    # Step 3: Sum up all adjusted values to get the final integer
    return reduce(lambda x, y: x + y, ls1)


# Example usage:

# Example 1:
# "XI" → X = 10, I = 1 → 10 + 1 = 11
print(romanToInt("XI"))   # Output: 11

# Example 2:
# "LXIX" → L = 50, X = 10, IX = 9 → 50 + 10 + 9 = 69
print(romanToInt("LXIX"))  # Output: 69

# Example 3:
# "MCMXCIV" → 1000 + (900) + (90) + (4) = 1994
print(romanToInt("MCMXCIV"))  # Output: 1994
