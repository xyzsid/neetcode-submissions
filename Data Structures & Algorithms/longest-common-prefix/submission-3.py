class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        #menstruation
        #menace
        #mending
        #meen
        #men

        #first string you put it in a stack
        #which i mean an array

        #and we compare the first few letters with each consecutive word

        #first letter where it defers is where we pop

        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res

            res += strs[0][i] 
        
        return res




                