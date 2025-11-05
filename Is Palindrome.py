# Given a string phrase, return True if it is a palindrome, otherwise return False.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Clarifications:
# phrase is made up of only: letters, numbers, spaces, and standard punctuation/symbols
# Example #1
# Input: phrase = "Taco cat."
# Output: True
# Explanation: Considering only alphanumeric characters and converting to lowercase, "tacocat" is a palindrome.

# Example #2
# Input: phrase = "I love SQL <3"
# Output: False
# Explanation: Considering only alphanumeric characters and converting to lowercase, "ilovesql3" is not even close.

def isPalindrome(phrase):
    # Remove all characters that are not letters or digits,
    # and convert everything to lowercase for a fair comparison
    no_spaces = ''.join(ch.lower() for ch in phrase if ch.isalnum())
    
    # Loop through the first half of the cleaned string
    for i in range(len(no_spaces) // 2):
        # Compare each character with its mirror character from the end
        if no_spaces[i] == no_spaces[-(i + 1)]:
            continue  # Characters match, keep checking
        else:
            return False  # Mismatch found — not a palindrome
    
    # If the loop completes without returning False, it's a palindrome
    return True


# Test the function with a phrase that *is* a palindrome
print(isPalindrome('Yo! Banana boy.'))  # Expected output: True
