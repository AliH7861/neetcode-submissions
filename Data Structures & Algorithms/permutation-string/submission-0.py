class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

      # Permutation of a String is any rearrangment of it's characters

      # In this problem we will need state
      # State should check if any version of abc exists 

      # So keep state, by checking frequency
      # If frequency of all three change, right after one another then return true
      # Or else return false

      # Define state

      left = 0
      need = {}
      window = {}

      for ch1 in s1:
       need[ch1] = need.get(ch1, 0) + 1

      
      for right in range (len(s2)):
        
        # Add new characters
        ch = s2[right]
        window[ch] = window.get(ch, 0) + 1

        # Remove Left Character if Block Bigger
        # Shift Window if size > 3
        while (right - left + 1 > len(s1)):
          # Select the most left element
          left_char = s2[left]
          # Minus the Count (The State)
          window[left_char] -=1
          if(window[left_char] == 0):
            del window[left_char]
          left +=1
        
        if(window == need):
          return True
        

      return False

        