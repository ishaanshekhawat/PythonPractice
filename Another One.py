# You are given an integer array digits, where each digits[i] is the ith digit of positive whole number. It is ordered from most significant to least significant digit.

# Return an array of digits of the number after adding another one to the input.

# Example #1
# Input: digits = [1, 2, 3]

# Output: [1, 2, 4]

# Example #2
# Input: digits = [6, 9]

# Output: [7, 0]

def another_one(digits):
    l = []
    for i in digits:
        l.append(str(i))
    num = int(''.join(l))
    num = num+1
    plusone = list(str(num))
    l1 = []
    for i in plusone:
        l1.append(int(i))
    return l1