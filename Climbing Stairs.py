# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize prev1 and prev2 to 1, representing the base cases:
        # prev1 = number of ways to reach the previous step (n-1)
        # prev2 = number of ways to reach the step before that (n-2)
        prev1, prev2 = 1, 1

        # Handle the base cases for n == 0 or n == 1
        if n == 0:
            return 0  # No steps to climb, so 0 ways
        elif n == 1:
            return 1  # Only 1 way to climb to the first step (take a single step)

        # For n >= 2, calculate the number of ways to reach each step from 2 to n
        else:
            # Loop through each step from 2 to n
            for i in range(2, n + 1):
                # The number of ways to reach the current step is the sum of the ways to reach
                # the previous step (prev1) and the step before that (prev2)
                current = prev1 + prev2

                # Update prev2 to be prev1 (moving one step forward)
                prev2 = prev1

                # Update prev1 to be the current number of ways (moving one step forward)
                prev1 = current

            # After the loop ends, prev1 contains the number of ways to reach step n
            return prev1
