# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed from the array.
# A consecutive sequence consists of elements where each element is exactly 1 greater than the previous element. The elements in the sequence can be selected from any position in the array and do not need to appear in their original order.

# Example #1
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive is [1, 2, 3, 4] which have a length of 4

# Example #2
# Input: nums = [3, 2]
# Output: 2
# Explanation: The longest consecutive is [2, 3] which have a length of 2

def longest_consecutive(nums):
    ls = []
    nums = list(set(nums))
    nums.sort()
    ct = 1
    for i in range(len(nums)-1):
        if nums[i] + 1 == nums[i+1]:
            ct += 1
        else:
            ct = 1
        ls.append(ct)
    return max(ls)
	
print(longest_consecutive([100, 4, 200, 1, 3, 2]))

print(longest_consecutive([3, 2]))

print(longest_consecutive([1,2,0,1]))

print(longest_consecutive([9,1,4,7,3,-1,0,5,8,-1,6]))

			