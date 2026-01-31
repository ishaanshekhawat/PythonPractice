# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        lengthy = len(strs[0])

        for i in strs[1:]:
            while i[:min([len(i), lengthy])] != strs[0][:lengthy]:
                lengthy -= 1

        return prefix[:lengthy]
