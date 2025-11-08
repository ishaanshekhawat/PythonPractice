# Given an integer array and an integer n as input, return the top n integers in the array 
# (the ones that appear most frequently). Return the output in non-decreasing order. 
# The test cases are generated in such a way that there will be a unique answer.

# Example #1
# Input: nums = [2, 1, 2, 3, 2, 1, 2, 1, 3, 4], n = 3
# Output: [1, 2, 3]

# Explanation: The most frequent elements are: 2 with a frequency of 4, 1 with a frequency of 3, and 3 with a frequency of 2. Finally, the output is sorted in non-decreasing order.

# Example #2
# Input: nums = [3, 2], n = 2
# Output: [2, 3]

def most_popular(nums, n):
	dict1 = {}
	for i in range(len(nums)):
		if nums[i] in dict1.keys():
			dict1[nums[i]] += 1
		else:
			dict1[nums[i]] = 1
	print(dict1)
	dict2 = dict(sorted(dict1.items(), key = lambda x: x[1], reverse=True))
	print(dict2)
	ct = 0
	ls = []
	for k,v in dict2.items():
		ls.append(k)
		ct += 1
		if ct == 3:
			break
	for i in range(len(ls)):
		for j in range(len(ls)-1):
			if ls[j] > ls[i]:
				ls[j],ls[i]=ls[i],ls[j]
	print(ls)
	
	
			
most_popular(nums = [2, 1, 2, 3, 2, 1, 2, 1, 3, 4, 4, 4], n = 3)