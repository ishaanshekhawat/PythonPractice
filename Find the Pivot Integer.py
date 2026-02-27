# https://leetcode.com/problems/find-the-pivot-integer/description/

class Solution:
    def pivotInteger(self, n: int) -> int:
        s1 = 0
        s2 = 0
        for i in range(1, n+1):
            s2 += i

        for i in range(1, n+1):
            s1 += i

            if s1 == s2:
                return i

            s2 -= i
        
        return -1
