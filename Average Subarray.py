# You are given an integer array nums consisting of n elements, and an integer k.

# Your task is to find a contiguous subarray of nums whose length is exactly k that 
# has the highest average value. A subarray is simply a sequence of consecutive elements from the original array. 
# After identifying this subarray, return the average value, rounded to two decimal places.

# Example #1
# Input: nums = [1, 2, -5, -3, 10, 3], k = 3

# Output: 3.33

# Explanation: The subarray here is [-3, 10, 3] , so the average is 3.33.

# Example #2
# Input: nums = [9], k = 1

# Output: 9.00

# Explanation: The subarray here is just [9], so its average is exactly 9.00.

from functools import reduce

def max_avg_subarray(nums, k):
	ls = []
	for i in range(len(nums)-k+1):
		ls.append(nums[i:i+k])
	dict1 = {}
	for i in ls:
		dict1[reduce(lambda x,y:x+y, i)] = i
	ct = -100000
	for i in dict1.keys():
		if i > ct:
			ct = i
	return round(reduce(lambda x,y:x+y, dict1[ct])/k,2)
