# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}

        for i in strs:
            srt = ''.join(sorted(i))
            if srt not in d:
                d[srt] = [i]
            else:
                d[srt].append(i)

        ls = []
        for k,v in d.items():
            ls.append(v)

        return ls
