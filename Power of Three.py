# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

class Solution(object):
    def isPowerOfThree(self, n):
        # If n is less than or equal to 0, it's not a power of three
        if n <= 0:
            return False
        
        # While n is divisible by 3, keep dividing it by 3
        while n % 3 == 0:
            n = n // 3  # Use integer division to avoid floating point numbers
        
        # If n becomes 1, then it was a power of 3 (since 3^x = 1 only when x = 0)
        if n == 1:
            return True
        
        # If n is not 1 after division, it's not a power of 3
        else:
            return False
