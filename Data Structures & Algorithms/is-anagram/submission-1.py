class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Basically compare two dict and see if they match or not
        sdict = {}
        tdict = {}
        # Go thru string s
        for a in s:
            sdict[a] = sdict.get(a, 0)  + 1
        
        for b in t:
            tdict[b] = tdict.get(b,0) + 1

        if sdict == tdict:
            return True
        else:
            return False
        