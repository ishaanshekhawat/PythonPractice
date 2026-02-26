# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/

class Solution:
    def numSteps(self, s: str) -> int:
        ls = list(s)
        
        for i in range(len(ls)):
            ls[i] = int(ls[i])
        
        i = 0

        ls.reverse()

        for j in range(len(ls)):
            i += ls[j]*2**j

        steps = 0

        while i != 1:
            if i % 2 == 0:
                i //= 2
            else:
                i += 1

            steps += 1
        
        return steps
