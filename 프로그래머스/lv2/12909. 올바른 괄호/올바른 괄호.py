def solution(s):
    answer = True
    stack = []
    top = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            top += 1
        else:
            if top != 0:
                if stack[top-1] == '(':
                    stack.pop()
                    top -= 1
            else:
                answer = False
                break
    
    if top != 0:
        answer = False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer