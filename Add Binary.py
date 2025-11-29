# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        extra_zeroes_on_left = []
        sol = []
        if len(a) != len(b):
            len_diff = len(a) - len(b)
            if len_diff > 0:
                for i in range(len_diff):
                    extra_zeroes_on_left.append('0')
                b = extra_zeroes_on_left + list(b)
                b = ''.join(b)
            else:
                for i in range(abs(len_diff)):
                    extra_zeroes_on_left.append('0')
                a = extra_zeroes_on_left + list(a)
                a = ''.join(a)
        a = str(a)
        b = str(b)
        carry = 0
        for i in range(1,len(a)+1):
            a_digit = int(a[-i])
            b_digit = int(b[-i])
            if a_digit + b_digit + carry == 2:
                carry = 1
                sol.append('0')
            elif a_digit + b_digit + carry == 3:
                carry = 1
                sol.append('1')
            else:
                sol.append(str(a_digit + b_digit + carry))
                if carry > 0:
                    carry -=1
        if carry == 1:
            sol.append('1')
        sol = sol[::-1]
        sol = ''.join(sol)
        return sol
