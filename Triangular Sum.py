# You are given an integer array nums, where each element in it is a single digit (0-9).
# The triangular sum of nums is the value of the only element present in nums after the following process terminates:
# Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new integer array newNums of length n - 1.
# For each index i, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes the modulo operator.
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the triangular sum of nums.
# Test Case #1:
# Input: nums = [1, 3, 5, 7]
# Iteration #1: Form newNums = [(1 + 3) % 10, (3 + 5) % 10, (5 + 7) % 10] = [4, 8, 2].
# Iteration #2: Form newNums = [(4 + 8) % 10, (8 + 2) % 10] = [2, 0].
# Iteration #3: Form newNums = [(2 + 0) % 10] = [2].
# The triangular sum of nums is 2.
# Test Case #2:
# Input: nums = [9, 7, 5, 3]
# Iteration #1: Form newNums = [(9 + 7) % 10, (7 + 5) % 10, (5 + 3) % 10] = [6, 2, 8].
# Iteration #2: Form newNums = [(6 + 2) % 10, (2 + 8) % 10] = [8, 0].
# Iteration #3: Form newNums = [(8 + 0) % 10] = [8].
# The triangular sum of nums is 8.

# Global list to store intermediate or final results
ls1 = []

# Helper function: performs one level of the triangular sum process
def temp(nums):
    ls = []  # Temporary list to store the new reduced list
    
    # Base case: if the list has only one element, it's the final triangular sum
    if len(nums) == 1:
        ls1.append(nums[0])
        return  # Stop further processing

    # Step 1: Create the next-level list using (nums[i] + nums[i+1]) % 10
    # This forms the new "layer" of the triangle
    for i in range(len(nums) - 1):
        ls.append((nums[i] + nums[i + 1]) % 10)
    
    # Step 2: If the new list still has more than one element, repeat the process
    while len(ls) > 1:
        triangular_sum(ls)  # Recursively call to process the next layer
        break  # Exit loop after one recursive call to avoid repetition
    
    # Step 3: Append the last reduced list to ls1 for later extraction
    ls1.append(ls)


# Main function: calculates the triangular sum of the input list
def triangular_sum(nums):
    # Step 1: Call helper function to begin recursive reduction
    temp(nums)
    
    # Step 2: If the stored result is a single integer, wrap it in a list for consistency
    if isinstance(ls1[0], int):
        ls1[0] = [ls1[0]]
    
    # Step 3: Extract and return the final triangular sum value
    for i in ls1[0]:
        return i


# Example test cases:

# Test Case 1:
# Input: [1, 3, 5, 7]
# Steps:
# [1, 3, 5, 7] → [4, 8, 2] → [2, 0] → [2]
# Output: 2
print(triangular_sum([1, 3, 5, 7]))  # Output: 2

# Test Case 2:
# Input: [9, 7, 5, 3]
# Steps:
# [9, 7, 5, 3] → [6, 2, 8] → [8, 0] → [8]
# Output: 8
print(triangular_sum([9, 7, 5, 3]))  # Output: 8


