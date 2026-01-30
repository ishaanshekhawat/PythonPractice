# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        alnum_s = []
        for i in s:
            if i.isalnum():
                alnum_s.append(i)
        
        alnum_s = ''.join(alnum_s)
        if alnum_s == alnum_s[::-1]:
            return True
        return False
