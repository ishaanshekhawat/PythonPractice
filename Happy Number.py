# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        dict1 = {}
        
        def digi_sq(num):
            sq = 0
            for i in str(num):
                sq += int(i) ** 2
            return sq
        
        while n != 1:
            if n in dict1:
                return False
            dict1[n] = 1
            n = digi_sq(n)
        
        return True
