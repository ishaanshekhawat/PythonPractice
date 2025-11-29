# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution(object):
    def plusOne(self, digits):
        # Start from the last digit using negative indexing
        i = -1
        ct = 0  # Counter for how many trailing 9s we have

        # Special case: if the number is exactly [9], result must be [1, 0]
        if digits == [9]:
            return [1, 0]

        # Case 1: last digit is 9 – we need to handle carries
        elif digits[-1] == 9:

            # Count how many trailing 9s the number has
            while digits[i] == 9:
                i -= 1
                ct += 1

                # If we've gone past the entire list, stop
                if abs(i) > len(digits):
                    break

            # Remove all trailing 9s
            for _ in range(ct):
                digits.pop()

            # If there are digits left, increment the new last digit
            if digits != []:
                last = digits[-1]
                digits.pop()
                digits.append(last + 1)
            else:
                # If all digits were 9, we start with 1
                digits.append(1)

            # Add zeros for each removed 9 (since 9 + 1 => 0 with carry)
            for _ in range(ct):
                digits.append(0)

        # Case 2: last digit is not 9 – simple increment
        else:
            last = digits[-1]
            digits.pop()
            digits.append(last + 1)

        return digits
