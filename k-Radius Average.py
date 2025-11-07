# You're given an array nums of n integers and an integer k.
# The k-radius average for a subarray of nums centered at some index i is the average of all elements from 
# indices i - k to i + k (inclusive). If there aren’t enough elements before or after index i to cover this radius, 
# the k-radius average is -1.
# Build and return an array averages of length n, where averages[i] contains the k-radius average for the 
# subarray centered at index i.
# Return your result rounded to 2 decimal places.
# p.s. before you tackle this challenge, maybe try this related warmup problem from Walmart 
# called Average Subarray (where you find the maximum average of any subarray of length k).

# Example #1
# Input: nums = [7, 2, 5, 12, 9, 4, 1], k = 2
# Output: [-1, -1, 7.0, 6.4, 6.2, -1, -1]

from functools import reduce

def k_radius_avg(nums, k):
    big_ls = []
    for i in range(len(nums)):
        ls = []
        if i - k < 0 or i + k >= len(nums):
            ls.append(-1)
        else:
            for j in range(i - k, i + k + 1):
                ls.append(nums[j])
        big_ls.append(ls)
    avg_ls = []
    for i in big_ls:
        avg_ls.append(round(reduce(lambda x, y: x + y, i) / len(i), 2))
    return avg_ls

print(k_radius_avg(nums = [7, 2, 5, 12, 9, 4, 1], k = 2))



