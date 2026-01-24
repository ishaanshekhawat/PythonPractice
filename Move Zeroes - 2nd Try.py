# https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        zeroes = nums.count(0)
        for i in range(zeroes):
            nums.remove(0)
        print(nums)
        print(zeroes)
        for i in range(zeroes):
            nums.append(0)
