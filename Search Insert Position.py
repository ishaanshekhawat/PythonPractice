# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution(object):
    def searchInsert(self, nums, target):
        # Initialize two pointers: left and right
        left = 0
        right = len(nums) - 1
        
        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If the target is found at the middle index, return that index
            if target == nums[mid]:
                return mid
            # If the target is greater than the middle element, 
            # move the left pointer to the right half
            elif target > nums[mid]:
                left = mid + 1
            # If the target is smaller than the middle element,
            # move the right pointer to the left half
            else:
                right = mid - 1
        
        # If the target is not found, return the index where the target would be inserted
        return left
