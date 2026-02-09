# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls = []
        pref = [1]
        mul = 1
        for i in range(1,len(nums)):
            mul*=nums[i-1]
            pref.append(mul)
        suf = []
        mul = 1
        for i in range(len(nums)-2,-1,-1):
            mul*=nums[i+1]
            suf.append(mul)
        suf = suf[::-1]
        suf.append(1)
        for i in range(len(nums)):
            ls.append(pref[i]*suf[i])
        return ls
