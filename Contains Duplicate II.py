# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1 = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in dict1:
                dict1[num].append(i)
            else:
                dict1[num] = [i]
        print(dict1)

        for key,v in dict1.items():
            if len(v) > 1:
                for i in range(len(v)-1):
                    for j in range(i+1, len(v)):
                        if abs(v[i]-v[j]) <= k:
                            return True
        
        return False
