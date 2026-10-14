# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                ct = 0
                for j in range(len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                    ct+=1
                if ct == len(needle):
                    return i
        
        return -1
