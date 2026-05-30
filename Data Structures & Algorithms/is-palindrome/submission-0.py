class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Convert uppercase to lowercase
        s2 = ''.join(ch.lower() for ch in s if ch.isalnum())

        # Set up the two pointers
        left = 0
        right = len(s2) - 1

        # Setting up While condition
        while left < right:
            if(s2[left] != s2[right]):
                return False
            left +=1
            right -=1

        return True

       
        