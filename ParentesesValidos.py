def is_valid(s):
    stack = []
    openTag = {'[': ']', '(': ')', '{': '}'}
    closeTag = {']': '[', ')': '(', '}': '{'}
    
    for char in s:
        if char in openTag:
            stack.append(char)
        elif stack and char == openTag[stack[-1]]:
            stack.pop()
        else:
            return False
    
    return not stack
s = "()"
print(is_valid(s))
s = "()[]{}"
print(is_valid(s))
s = "(]"
print(is_valid(s))