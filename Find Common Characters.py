# https://leetcode.com/problems/find-common-characters/description/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def inter(ls1, ls):
            j = 0
            while j < min([len(ls1), len(ls)]):
                if ls1[j] == ls[j]:
                    j+=1
                elif ls1[j] < ls[j]:
                    ls1.pop(j)
                else:
                    ls.pop(j)
            
            if len(ls1) < len(ls):
                return ls1
            else:
                return ls

        
        ls = list(words[0])
        ls.sort()
        
        for i in range(1,len(words)):
            ls1 = list(words[i])
            ls1.sort()

            if ls1 == ls:
                continue
            else:
                ls = inter(ls1, ls)

        return ls
