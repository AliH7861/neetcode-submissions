class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}

        for element in s:
            # Append if its opening brackets
            if element in '([{':
                stack.append(element)
            else:
                # Check if its a stack
                # Check if last element is not one of the pairs
                if not stack or stack[-1] != pairs[element]:
                    return False
                # Pop the element
                stack.pop()
            
        
        # Return when the stack is empty
        return len(stack) == 0