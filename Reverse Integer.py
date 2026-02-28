# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            s = str(x)
            s = s[::-1]
        else:
            s = str(x*-1)
            s = s[::-1]
            s = '-' + s
        
        if int(s) > (2**31 - 1) or int(s) < (-2**31):
            return 0
        return int(s)
