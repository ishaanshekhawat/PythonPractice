# http://leetcode.com/problems/find-the-duplicate-number/description/Find%20the%20Duplicate%20Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                return i
            else:
                d[i] = 1
