# Given an integer array, find the sum of the largest contiguous subarray within the array.

# For example, if the input is [−1, −3, 5, −4, 3, −6, 9, 2], then return 11 (because of [9, 2]).

# Note that if all the elements are negative, you should return 0.

def max_subarray_sum(input):
	sum = 0
	max = 0
	ct = 0
	for i in input:
		if i < 0:
			ct += 1
		if sum + i < 0:
			sum = 0
		else:
			sum += i
		if sum > max:
			max = sum
	if ct == len(input):
		return 0
	return max

print(max_subarray_sum([1, -1, 1, -1, 1, -1, 5]))