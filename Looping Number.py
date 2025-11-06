# Given an integer n, check if it is a looping number. A looping number has the following properties:

# It is repeatedly replaced by the sum of the squares of its digits.
# This process continues until:
# The number becomes 1, in which case it is not a looping number.
# The number starts repeating in a cycle that does not include 1, making it a looping number.
# Return True if n is a looping number, otherwise return False.

# Example #1
# Input: n = 4
# Output: True
# Since the number loops back to 4, it is a looping number.

# Example #2
# Input: n = 19
# Output: False
# Since the number reaches 1, it is not a looping number.

def digit_square(num):
	sum = 0
	for i in num:
		digit = int(i)
		sum += digit**2
	return sum

ls = []

def is_looping(n):
    if digit_square(str(n)) == 1:
        return False
    elif digit_square(str(n)) in ls:
        return True
    else:   
        ls.append(digit_square(str(n)))
    return is_looping(digit_square(str(n)))
        
print(is_looping(19))
print(is_looping(4))
	
		

