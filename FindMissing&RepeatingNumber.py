# You’re given a list of integers nums of length n where each integer is in the range [1, n].
# One number appears twice, and one number is missing.
# Your task is to find both numbers.

# Read a line of space-separated integers from input and convert them into a list
nums = list(map(int, input().split()))

# Step 1: Find the missing number
# Iterate through numbers from 1 to n (inclusive)
for i in range(1, len(nums) + 1):
    # If a number i is not present in nums, it's the missing one
    if i not in nums:
        missing = i
        break  # Stop once we find the missing number

# Step 2: Find the repeated number
# Again iterate through numbers from 1 to n (inclusive)
for i in range(1, len(nums) + 1):
    # If a number appears twice, it's the repeated one
    if nums.count(i) == 2:
        repeated = i
        break  # Stop once we find the repeated number

# Print the results
print(missing)   # Output the missing number
print(repeated)  # Output the repeated number
