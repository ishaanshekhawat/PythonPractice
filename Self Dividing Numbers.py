# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        l2 = []
        
        def inner(l2, num):
            l1 = []
            for i in str(num):
                l1.append(int(i))

            ct = 0

            for i in l1:
                if i == 0:
                    break
                if num % i == 0:
                    ct+=1

            if ct == len(l1):
                l2.append(num)

        for i in range(left, right + 1):
            inner(l2, i)
        
        return l2
