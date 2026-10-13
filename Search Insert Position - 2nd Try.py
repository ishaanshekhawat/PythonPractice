# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        cur_index = 0
        while cur_index < len(nums) and nums[cur_index] <= target:
            if nums[cur_index] == target:
                return cur_index
            
            cur_index += 1
        
        return cur_index
