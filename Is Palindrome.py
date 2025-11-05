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
    no_spaces = ''.join(ch.lower() for ch in phrase if ch.isalnum())
    for i in range(len(no_spaces)//2):
        if no_spaces[i] == no_spaces[-(i+1)]:
            continue
        else:
            return False
    return True

print(isPalindrome('Yo! Banana boy.'))