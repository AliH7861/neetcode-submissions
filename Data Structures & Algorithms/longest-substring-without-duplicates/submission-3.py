class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        output = 0

        countSet = set()

        for right in range (0, len(s)):
            
            while s[right] in countSet:
                # Move the window to current position
                countSet.remove(s[left])
                left+=1
          
            # If its not in set you add value
            output = max(output, (right - left + 1))
            countSet.add(s[right])
            
        # Return the output
        return output