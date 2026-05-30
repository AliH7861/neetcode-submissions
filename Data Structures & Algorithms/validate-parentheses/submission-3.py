class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if (len(stack) == 0 or stack[-1] != close_to_open[ch]):
                    return False
                stack.pop()
        return len(stack) == 0
     

     



        