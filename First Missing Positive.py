# https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ct = 1
        for i in range(len(nums)):
            if nums[i] == ct:
                ct+=1
        return ct
