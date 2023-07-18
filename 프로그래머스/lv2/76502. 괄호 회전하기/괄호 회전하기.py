def is_correct(s):
    stack = []
    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if char == ')' and top != '(':
                return False
            elif char == ']' and top != '[':
                return False
            elif char == '}' and top != '{':
                return False
    return len(stack) == 0

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_correct(rotated):
            answer += 1
    return answer