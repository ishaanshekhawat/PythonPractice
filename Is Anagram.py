# Given two strings s and t, return True if the two strings are anagrams of each other, otherwise return False.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
# You can assume both of the strings will contain lowercase alphabet characters.
# Example #1
# Input: s = "listen", t = "silent"
# Output: True
# Example #2
# Input: s = "astronomer", t = "moonstarer"
# Output: True
# Example #3
# Input: s = "lemur", t = "lemer"
# Output: False
        
# Function to check if two strings are anagrams of each other
def is_anagram(s, t):
    # Sort both strings alphabetically
    # Example: "listen" → ['e', 'i', 'l', 'n', 's', 't']
    s1 = sorted(s)
    t1 = sorted(t)
    # Compare the sorted versions of both strings
    # If they are identical, it means they contain the same letters
    if s1 == t1:
        return True   # Strings are anagrams
    return False       # Strings are not anagrams
