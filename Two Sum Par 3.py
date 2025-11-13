# Given an array of integers nums and an integer k, return the largest possible maxSum < k such that 
# maxSum = nums[i] + nums[j] and i ≠ j. If no maxSum < k is possible, return -1.

# Example #1
# Input: nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60
# Output: 58
# Explanation: The greatest possible sum less than 60 is 58, made by adding 34 + 24

def max_two_sum(nums, k):
	maxSum = float('-inf')
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] < k and maxSum < nums[i] + nums[j]:
				maxSum = nums[i] + nums[j]
	if maxSum != float('-inf'):
		return maxSum
	return -1

