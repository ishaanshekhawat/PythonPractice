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

        # List to hold extra zeros for left-padding the shorter string
        extra_zeroes_on_left = []

        # List to accumulate the resulting binary digits (in reverse)
        sol = []

        # --- STEP 1: Pad the shorter string with leading zeros ---
        if len(a) != len(b):
            len_diff = len(a) - len(b)

            # Case: a is longer → pad b
            if len_diff > 0:
                for i in range(len_diff):
                    extra_zeroes_on_left.append('0')

                # Convert b to list, prepend zeros, then join back to string
                b = extra_zeroes_on_left + list(b)
                b = ''.join(b)

            # Case: b is longer → pad a
            else:
                for i in range(abs(len_diff)):
                    extra_zeroes_on_left.append('0')
                a = extra_zeroes_on_left + list(a)
                a = ''.join(a)

        # --- STEP 2: Add digits from right to left (binary addition) ---
        carry = 0

        # Loop from last character to first
        for i in range(1, len(a) + 1):
            # Convert the ith digits from the right into integers
            a_digit = int(a[-i])
            b_digit = int(b[-i])

            # Sum the bits plus carry
            total = a_digit + b_digit + carry

            # Handle binary addition outcomes
            if total == 2:
                # 1 + 1 (+0) → write 0, carry 1
                carry = 1
                sol.append('0')
            elif total == 3:
                # 1 + 1 + 1 → write 1, carry 1
                carry = 1
                sol.append('1')
            else:
                # total is 0 or 1 → write it
                sol.append(str(total))
                # If carry was used (total=1 and carry came from earlier), reset carry
                if carry > 0:
                    carry -= 1

        # --- STEP 3: If leftover carry remains, append it ---
        if carry == 1:
            sol.append('1')

        # Bits were added in reverse order → reverse to restore correct order
        sol = sol[::-1]

        # Convert list of chars to a string
        sol = ''.join(sol)

        return sol
