# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

class Solution(object):
    def moveZeroes(self, nums):
        # Initialize a counter for non-zero elements
        ct = 0
        
        # Iterate over the list 'nums'
        for i in nums:
            # If the current element is 0
            if i == 0:
                # Append 0 to the end of the list
                nums.append(0)
                # Remove the first occurrence of 0 from the list
                nums.remove(i)
        
        # The modified list is updated in place, no need to return anything.
        return nums  # This is technically unnecessary as the list is modified in-place.
