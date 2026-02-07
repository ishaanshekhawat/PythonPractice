# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for i in strs:
            a = ''.join(sorted(i))

            if a not in d:
                d[a] = []
            d[a].append(i)
        
        return list(d.values())
