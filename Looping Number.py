# Given an integer n, check if it is a looping number. A looping number has the following properties:
# - The number is repeatedly replaced by the sum of the squares of its digits.
# - This process continues until:
#   * The number becomes 1  → it is NOT a looping number.
#   * The number starts repeating (enters a cycle) that does NOT include 1 → it IS a looping number.
# Return True if n is a looping number, otherwise return False.

# Example #1
# Input: n = 4
# Output: True
# Explanation: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 (loops back to 4)
# So, it is a looping number.

# Example #2
# Input: n = 19
# Output: False
# Explanation: 19 → 82 → 68 → 100 → 1
# Since it reaches 1, it is not a looping number.


# Helper function to calculate the sum of the squares of digits of a number
def digit_square(num):
    total = 0  # Initialize the sum
    for i in num:  # Iterate through each digit (num is passed as a string)
        digit = int(i)
        total += digit ** 2  # Add the square of the digit
    return total  # Return the sum of squares


# Global list to keep track of previously seen numbers (to detect a loop)
ls = []


def is_looping(n):
    """
    Recursively determines if the given number n is a looping number.
    """
    # Base case: if sum of squares equals 1 → it’s not a looping number
    if digit_square(str(n)) == 1:
        return False

    # If the sum of squares has already appeared, a loop is detected → looping number
    elif digit_square(str(n)) in ls:
        return True

    else:
        # Store the result in the list to track visited numbers
        ls.append(digit_square(str(n)))

    # Recursively call the function with the next number (sum of squares)
    return is_looping(digit_square(str(n)))


# Test cases
print(is_looping(19))  # Expected output: False (reaches 1)
print(is_looping(4))   # Expected output: True (enters a loop)
