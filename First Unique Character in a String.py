# https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}
        for i in list(s):
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        val = ''
        for k,v in dict1.items():
            if v == 1:
                val = k
                break
        
        temp = list(s)
        for i in range(len(temp)):
            if temp[i] == val:
                return i
        
        return -1
