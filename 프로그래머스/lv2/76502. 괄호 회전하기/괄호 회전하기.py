def solution(st):
    answer = 0
    for i in range(len(st)):
        s = st[i:] + st[:i]
        stack = []
        top = 0
        nocorrect = 0
        for j in range(len(s)):
            if s[j] == ']':
                if top > 0 and stack[top-1] == '[':
                    stack.pop()
                    top -= 1
                else:
                    nocorrect = 1
                    break
            elif s[j] == ')':
                if top > 0 and stack[top-1] == '(':
                    stack.pop()
                    top -= 1
                else:
                    nocorrect = 1
                    break
            elif s[j] == '}':
                if top > 0 and stack[top-1] == '{':
                    stack.pop()
                    top -= 1
                else:
                    nocorrect = 1
                    break
            else:
                stack.append(s[j])
                top += 1
                    
        if nocorrect == 1 or len(stack) != 0:
            nocorrect = 0
        else:
            answer += 1
            
    return answer