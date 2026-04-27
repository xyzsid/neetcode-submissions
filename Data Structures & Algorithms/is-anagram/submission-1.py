class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}

        for i in s:
            if i in dicts:
                dicts[i] = dicts[i] + 1
            else:
                dicts[i] =  1

        for j in t:
            if j in dicts:
                dicts[j] = dicts[j] - 1
            else:
                return False
        x = dicts.values()

        for z in x:
            if z !=0:
                return False
        return True
        

