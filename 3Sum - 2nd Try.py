# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ls = set()
        for i in range(len(nums)-1):
            seen = set()
            for j in range(i+1,len(nums)):
                complement = (-nums[j]) + (-nums[i])
                if complement in seen:
                    ls.add((nums[i], nums[j], complement))
                seen.add(nums[j])

        return list(map(list, ls))
