# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        sd = dict(sorted(d.items(), key = lambda x: x[1], reverse=True))
        
        ls = []
        print(sd)
        for key,v in sd.items():
            ls.append(key)
            if len(ls) == k:
                break
        
        return ls
