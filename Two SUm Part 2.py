# You are given an array of integers nums sorted in non-decreasing order, 
# meaning that each value is equal to or greater than the one before it.
# Return the indices of the two values in nums that add up to a given target number.

# Clarifications:
# There is at most one solution.
# If there is no valid solution, return [-1, -1].
# Return the indices in increasing order (i.e. [1,3], NOT [3,1]).
# Your solution must use constant extra space. This means that the size of any objects that you create 
# while solving the problem cannot grow with the length of nums. As a result, you won't be able to just 
# use your solution from the original Two Sum problem.

# Example #1
# Input: nums = [1, 3, 4, 5, 7, 12, 15] , target = 9
# Output: [2,3]
# Explanation: The values at indices 2 and 3 (4 and 5, respectively) add up to 9.

def sorted_two_sum(nums, target):
    # Iterate through the list of numbers
    for i in range(len(nums)-1):
        # Check all subsequent numbers after the current number at index i
        for j in range(i+1, len(nums)):
            # If the sum of the two numbers at indices i and j equals the target
            if nums[j] == target - nums[i]:
                # Return the indices of these two numbers
                return [i, j]
    # If no pair was found that adds up to the target, return [-1, -1]
    return [-1, -1]
