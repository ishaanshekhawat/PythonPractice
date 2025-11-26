# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

class Solution(object):
    # Method to convert a number into its binary representation as a list
    def numToBinaryList(self, num):
        ls = []  # List to store the binary digits (0 or 1)
        
        # If num is less than 2, it's already in binary form (0 or 1)
        if num < 2:
            ls = [num]  # Just return the number as a single-element list
            return ls
        
        # Keep dividing the number by 2, storing the remainder (binary digit)
        while num != 1:
            ls.append(num % 2)  # Append the remainder (either 0 or 1) to the list
            num = num // 2  # Divide the number by 2 using integer division
        
        # Append the last digit (1) to the list as the loop stops when num becomes 1
        ls.append(1)
        
        # Reverse the list to get the correct binary order (most significant bit first)
        return ls[::-1]

    # Method to count the number of 1's in the binary representation of all numbers from 0 to n
    def countBits(self, n):
        res = []  # List to store the count of 1's for each number from 0 to n
        
        # Loop through all numbers from 0 to n (inclusive)
        for i in range(n + 1):
            # Convert the current number to its binary list representation
            binaryList = self.numToBinaryList(i)
            
            ct = 0  # Counter for the number of 1's in the binary representation
            
            # Count the number of 1's in the binary list
            for j in binaryList:
                if j == 1:
                    ct += 1
            
            # Append the count of 1's to the result list
            res.append(ct)
        
        # Return the list containing the counts of 1's for each number from 0 to n
        return res
