
def is_valid_parenthese(s):
    if s is None:
        return False

    if not isinstance(s, str):
        return False

    if len(s) == 0:
        return True

    openers = ['(', '{', '[']
    closers = [')', '}', ']']

    stack = []
    for ch in s:
        if ch in openers:
            stack.append(ch)
        elif ch in closers:
            if len(stack) == 0:
                return False
            top = stack[-1]

            if ch == ')' and top == '(':
                stack.pop()
            elif ch == '}' and top == '{':
                stack.pop()
            elif ch == ']' and top == '[':
                stack.pop()
            else:
                return False
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False
