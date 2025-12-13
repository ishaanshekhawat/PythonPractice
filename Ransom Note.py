# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rs_ls = list(ransomNote)
        m_ls = list(magazine)

        rs_ls = sorted(ransomNote)
        m_ls = sorted(magazine)

        k = 0

        print(rs_ls)
        print(m_ls)

        for i in range(len(m_ls)):
            if rs_ls[k] == m_ls[i]:
                k += 1
            if k == len(rs_ls):
                return True
        
        return False
