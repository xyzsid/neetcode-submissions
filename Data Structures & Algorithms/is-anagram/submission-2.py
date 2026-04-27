class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this is for s
        # make a hashmap and make each letter a key and init hash with 1 if we have that letter
        # increment each letter with hash as seen fit

        # make the same dictionary for t
        # the same way me made dict for s

        # at the end we compare the two dicts

        # Space: O(n)
        # Time:  O()

        sdict = {}
        tdict = {}

        for letter in s:
            if letter in sdict:
                sdict[letter] += 1
            else:
                sdict[letter] = 1

        
        for letter in t:
            if letter in tdict:
                tdict[letter] += 1
            else:
                tdict[letter] = 1

        return sdict == tdict