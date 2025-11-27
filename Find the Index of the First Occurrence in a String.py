# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution(object):
    def strStr(self, haystack, needle):
        # If haystack and needle are exactly the same, return 0 (first occurrence at index 0)
        if haystack == needle:
            return 0
        else:
            # Loop through the haystack, checking if the substring starting from each index matches the needle
            # We only need to check up to len(haystack) - len(needle) + 1 to avoid out-of-bounds errors
            for i in range(len(haystack)-len(needle)+1):
                # Check if the substring of haystack starting at index i matches needle
                if haystack[i:i+len(needle)] == needle:
                    # If a match is found, return the starting index i
                    return i
        # If no match is found, return -1
        return -1
