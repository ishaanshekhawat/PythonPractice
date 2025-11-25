# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Loop through each index in the array except the last one
        for i in range(len(nums) - 1):
            
            # Compare element at index i with every element after it
            for j in range(i + 1, len(nums)):
                
                # If a smaller value is found, swap so smaller values move forward
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        # Although LeetCode expects in-place modification and no return,
        # returning nums doesn't cause issues.
        return nums
