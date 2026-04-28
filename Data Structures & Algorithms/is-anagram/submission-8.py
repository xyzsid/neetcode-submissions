class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_one = {}
        dict_two = {}

        for char in s:
            if char in dict_one:
                dict_one[char] += 1
            else:
                dict_one[char] = 1

        for char in t:
            if char in dict_two:
                dict_two[char] += 1
            else:
                dict_two[char] = 1        
        
        return dict_one == dict_two