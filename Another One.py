# You are given an integer array digits, where each digits[i] is the ith digit of positive whole number. It is ordered from most significant to least significant digit.

# Return an array of digits of the number after adding another one to the input.

# Example #1
# Input: digits = [1, 2, 3]

# Output: [1, 2, 4]

# Example #2
# Input: digits = [6, 9]

# Output: [7, 0]

def another_one(digits):
    # Initialize an empty list to store digits as strings
    l = []
    
    # Convert each integer digit to a string and append it to the list
    for i in digits:
        l.append(str(i))
    
    # Join all string digits into one full number string, then convert it to an integer
    num = int(''.join(l))
    
    # Add one to the integer
    num = num + 1
    
    # Convert the incremented number back into a list of string digits
    plusone = list(str(num))
    
    # Initialize another list to store the final digits as integers
    l1 = []
    
    # Convert each string digit back into an integer
    for i in plusone:
        l1.append(int(i))
    
    # Return the list of digits representing the incremented number
    return l1
