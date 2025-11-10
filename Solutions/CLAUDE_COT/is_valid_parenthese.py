def is_valid_parenthese(s):
    """Check if a string of parentheses is valid."""
    stack = []
    matching = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in matching:
            stack.append(char)
        elif char in matching.values():
            if not stack:
                return False
            if matching[stack.pop()] != char:
                return False
    
    return len(stack) == 0
