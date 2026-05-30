class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Define array
        counts = [0] * 26
        countt = [0] * 26
        # For Loop 1
        for chas in s:
            indexs = ord(chas) - ord('a')
            counts[indexs] += 1


        # For Loop 2
        for chat in t:
            indext = ord(chat) - ord('a')
            countt[indext] +=1
        
        # If Statement
        if(counts == countt):
            return True
        else:
            return False


        
        

        

        