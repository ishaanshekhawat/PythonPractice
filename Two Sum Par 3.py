# Given an array of integers nums and an integer k, return the largest possible maxSum < k such that 
# maxSum = nums[i] + nums[j] and i ≠ j. If no maxSum < k is possible, return -1.

# Example #1
# Input: nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60
# Output: 58
# Explanation: The greatest possible sum less than 60 is 58, made by adding 34 + 24

def max_two_sum(nums, k):
	# Initialize maxSum to negative infinity to represent no valid sum found yet
	maxSum = float('-inf')

	# Iterate through all possible pairs (i, j) where i < j
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			# Check if the current pair sum is less than k 
			# and greater than the current maxSum found so far
			if nums[i] + nums[j] < k and maxSum < nums[i] + nums[j]:
				# Update maxSum with this new valid pair sum
				maxSum = nums[i] + nums[j]

	# If we found at least one valid pair, return the largest sum found
	if maxSum != float('-inf'):
		return maxSum

	# If no valid pair sum < k was found, return -1
	return -1
