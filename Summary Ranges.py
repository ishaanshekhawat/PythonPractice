# https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ls = []
        ct = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if ct == 0:
                    ls.append([nums[i]])
                else:
                    ls.append(nums[i-ct:i+1])
                break

            if nums[i] == nums[i+1]-1:
                ct += 1
            else:
                if ct != 0:
                    ls.append(nums[i-ct:i+1])
                    ct = 0
                else:
                    ls.append([nums[i]])
        print(ls)
        ls1 = []
        for i in ls:
            if len(i) > 1:
                ls1.append(f"{i[0]}->{i[-1]}")
            else:
                ls1.append(str(i[0]))
        
        return ls1
