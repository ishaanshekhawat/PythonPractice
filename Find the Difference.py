# https://leetcode.com/problems/find-the-difference/description/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ls1 = list(s)
        ls2 = list(t)

        ls1.sort()
        ls2.sort()

        for i in range(len(ls1)):
            if ls2[i] != ls1[i]:
                return ls2[i]
        
        return ls2[-1]
