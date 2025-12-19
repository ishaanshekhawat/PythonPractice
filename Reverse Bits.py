# Reverse bits of a given 32 bits signed integer.

# Example 1:

# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	        Binary
# 43261596	      00000010100101000001111010011100
# 964176192    	  00111001011110000010100101000000

# Example 2:
# Input: n = 2147483644
# Output: 1073741822
# Explanation:
# Integer	        Binary
# 2147483644	    01111111111111111111111111111100
# 1073741822	    00111111111111111111111111111110

class Solution:
    def createBinary(self, i: int) -> str:
        ls = []
        if i == 0:
            return '0'
        elif i == 1:
            return '1'
        else:
            while i > 0:
                if i % 2 == 1:
                    ls.append('1')
                else:
                    ls.append('0')
                i = i // 2
        s = ''.join(ls[::-1])
        s = s.rjust(32,'0')
        return s
            

    def reverseBits(self, n: int) -> int:
        bin_n = self.createBinary(n)
        print(bin_n)
        rev_bin_n = bin_n[::-1]
        print(rev_bin_n)
        res = 0
        for i in range(len(rev_bin_n)):
            pw = len(rev_bin_n) - (i+1)
            num = int(rev_bin_n[i])
            res += num * 2 ** pw
            print(res, num, pw)
        return res
