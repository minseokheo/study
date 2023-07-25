def solution(s):
    answer = -1
    stack = []
    top = 0
    
    for c in s:
        if top == 0:
            stack.append(c)
            top += 1
        elif stack[top-1] != c:
            stack.append(c)
            top += 1
        elif stack[top-1] == c:
            stack.pop()
            top -= 1
    
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
        
    return answer