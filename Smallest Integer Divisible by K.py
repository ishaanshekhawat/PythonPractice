# https://leetcode.com/problems/smallest-integer-divisible-by-k/description/

# In the Smallest Repunit Divisible by K problem:
# We repeatedly compute remainders:
#     remainder = (previous_remainder * 10 + 1) % k
# Possible remainders when dividing by k are:
#     0, 1, 2, ..., k-1
# So there are k possible remainders (these are the “holes”).
# But we compute up to k remainders (these are the “pigeons”).
# If none of them is 0, then:
#     Two remainders must be the same (by the pigeonhole principle).
# Once a remainder repeats, the sequence cycles.
# If we didn’t hit 0 before the cycle, we never will.
# That’s why checking up to k iterations is enough.

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        rem = 0

        for i in range(1, k+1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return i
                
        return -1
