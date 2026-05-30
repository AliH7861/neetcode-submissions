class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
       

        # For every loop we go thru each letter of the string, and we append
        # the final count to the countArr
        # At the end of it, you would have all the elements
        for word in strs:
            count = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                count[index] +=1

            key = tuple(count)
            if key not in group:
                group[key] = []
            group[key].append(word)

        result = sorted(group.values(), key=len)
        return result
        
        
        