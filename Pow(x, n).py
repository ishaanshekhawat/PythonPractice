# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the edge case where n is 0
        if n == 0:
            return 1
        
        # Handle negative exponents
        if n < 0:
            x = 1 / x
            n = -n
        
        # Use exponentiation by squaring
        result = 1
        while n > 0:
            if n % 2 == 1:  # If n is odd, multiply by x
                result *= x
            x *= x  # Square x
            n //= 2  # Divide n by 2
        
        return result
