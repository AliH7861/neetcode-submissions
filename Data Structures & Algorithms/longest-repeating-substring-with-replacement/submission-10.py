class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        maxFreq = 0
        count = {}
        Output = 0

        for right in range (0, len(s)):
            # Maintaining a Count of Things
            count[s[right]] = count.get(s[right], 0) + 1
            maxFreq = max(maxFreq, count[s[right]])

            # Establishing a while loop
            # Loop states, all elements - maxElements - k is > 0
            while ((right - left + 1) - maxFreq) > k:
                count[s[left]] -=1
                left+=1

            # Establishing Output
            Output = max(Output, right - left  + 1)
        return Output
                
        