# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)

        ls.sort()
        lt.sort()

        if ls == lt:
            return True
        else:
            return False
