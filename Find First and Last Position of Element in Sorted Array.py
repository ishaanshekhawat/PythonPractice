# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):
        # Initialize two pointers: start and end
        start = 0
        end = len(nums) - 1
        
        # Loop while the start pointer is less than or equal to the end pointer
        while start <= end:
            # If both start and end point to the target, return the range [start, end]
            if nums[start] == target and nums[end] == target:
                return [start, end]
            
            # If the start pointer points to the target but the end doesn't, move the end pointer leftward
            elif nums[start] == target:
                end -= 1
            
            # If the end pointer points to the target but the start doesn't, move the start pointer rightward
            elif nums[end] == target:
                start += 1
            
            # If neither pointer points to the target, move both pointers inward
            else:
                start += 1
                end -= 1
        
        # If no range is found, return [-1, -1]
        return [-1, -1]
