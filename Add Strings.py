# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = list(num1)
        l2 = list(num2)

        max_len = max(len(num1),len(num2))

        if len(num1) > len(num2):
            l2 = [str(0)]*(len(num1) - len(num2)) + l2
        else:
            l1 = [str(0)]*(len(num2) - len(num1)) + l1

        carry = 0
        res = []
        for i in range(max_len-1,-1,-1):
            cur_sum = int(l1[i]) + int(l2[i]) + carry
            if i == 0:
                if cur_sum > 9:
                    res.append(cur_sum%10)
                    res.append(1)
                    break
                else:
                    res.append(cur_sum)
                    break
            
            if cur_sum > 9:
                carry = 1
                last_digit = cur_sum % 10
            else:
                carry = 0
                last_digit = cur_sum
            
            res.append(last_digit)
                   
        for i in range(len(res)):
            res[i] = str(res[i]) 
        
        return ''.join(res[::-1])
