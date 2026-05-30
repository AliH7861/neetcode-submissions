class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Setup the window
        seen = set()

        # Set the variables
        # Left side of the window
        left = 0

        # The maximum length
        maxLength = 0

        for right in range (len(s)):
            
            # Case 1: right letter is in seen
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            
            # Case 2: right letter is not in sen
            seen.add(s[right])

            # Compare both existing and normal
            maxLength = max(maxLength, right - left + 1)

        return maxLength 
