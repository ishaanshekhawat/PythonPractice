# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # List to collect characters that are part of the common prefix
        sol = []
        
        # Determine the length of the shortest string in the list
        # (The common prefix cannot be longer than this.)
        min_len = float('inf')
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        
        # Iterate index-by-index up to the shortest string's length
        for i in range(min_len):
            ct = 1  # Counter tracks how many adjacent string pairs match at position i
            
            # Compare each pair of neighboring strings at index i
            for j in range(len(strs) - 1):
                # If characters match, increase counter
                if strs[j][i] == strs[j + 1][i]:
                    ct += 1
                else:
                    # A mismatch means the common prefix ends here
                    break
            
            # If all strings matched at index i, add this character to the prefix
            if ct == len(strs):
                sol.append(strs[0][i])
            else:
                # First mismatch stops the search
                break
        
        # Convert list of characters back into a string and return
        return ''.join(sol)
