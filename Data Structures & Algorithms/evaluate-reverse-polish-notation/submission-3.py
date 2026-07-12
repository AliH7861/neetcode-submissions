class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Empty stack
        stack = []
        count = 0
        result = 0

        # For every token in tokens:
        for token in tokens:
            # If Its tokens perform the calculation
            if token in {'+', '-', '*', '/'}:

                # Define left and right
                right = stack.pop()
                left = stack.pop()

                # Perform Calculations
                if token == '+':
                    result = left + right
                    stack.append(result)
                elif token == '-':
                    result = left - right
                    stack.append(result)
                elif token == '*':
                    result = left * right
                    stack.append(result)
                else:
                    result = int(left / right)
                    stack.append(result)
            else:
                # Here if its number place it in stack
                stack.append(int(token))
    
        # Return Result
        final = stack.pop()
        return  final



        