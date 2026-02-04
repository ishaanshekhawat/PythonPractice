# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        def isAna(str1,str2):
            ls1 = list(str1)
            ls1.sort()
            ls2 = list(str2)
            ls2.sort()

            return ls1 == ls2
        
        left = 0
        right = 1
        while right < len(words):
            if isAna(words[left],words[right]):
                words.remove(words[right])
            else:
                left+=1
                right+=1
        
        return words
