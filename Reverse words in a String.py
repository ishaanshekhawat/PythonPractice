# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        s1 = ' '.join(ls[::-1])
        return s1
