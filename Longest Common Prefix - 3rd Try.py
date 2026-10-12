# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref = strs[0]
        for i in range(1, len(strs)):
            if len(pref) > len(strs[i]):
                pref = pref[:len(strs[i])]

            for j in range(min(len(strs[i]), len(pref))):
                if strs[i][j] != pref[j]:
                    pref = pref[:j]
                    break

        return pref
