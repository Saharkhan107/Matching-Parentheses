def is_balanced(expression):
    # Create a stack to hold opening symbols
    stack = []
    
    # Dictionary to match closing symbols with opening symbols
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the expression
    for char in expression:
        if char in matching_brackets.values():
            # If it's an opening symbol, push it to the stack
            stack.append(char)
        elif char in matching_brackets.keys():
            # If it's a closing symbol, check if it matches the top of the stack
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # Pop the opening symbol from the stack
            else:
                return False  # Mismatched or unbalanced parenthesis, return False
                
    # If the stack is empty, all symbols were matched correctly
    return len(stack) == 0

# Test cases
print(is_balanced("{[()]}"))  # Expected output: True
print(is_balanced("{[(])}"))  # Expected output: False
print(is_balanced("{[}"))     # Expected output: False
print(is_balanced("()[]{}"))  # Expected output: True
print(is_balanced("((()))"))  # Expected output: True
print(is_balanced("({[()]})"))  # Expected output: True

