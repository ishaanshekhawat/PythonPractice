# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        d2 = dict(sorted(d.items(), key = lambda x: x[1], reverse=True))

        l1 = []
        ct=0
        for key,v in d2.items():
            if ct==k:
                break
            l1.append(key)
            ct+=1
            
        
        return l1
            

        
