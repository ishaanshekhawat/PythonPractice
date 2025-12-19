class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If the number is negative, it's not a palindrome
        if x < 0:
            return False
        
        # Convert the integer to string and check if it's the same forwards and backwards
        return str(x) == str(x)[::-1]
