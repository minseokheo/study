# 문제를 처음 접근했을때는 1~4번까지 규칙을 순서대로 만족시켜주면 해결되는 문제로 생각하였습니다.
## 문제를 풀고 질문하기를 들어가보고 다시 문제를 읽어보니 4-2 부분에 대한 문제를 잘 해결하지 못했고 다시 수정했습니다.
def isCorrectString(u):
    u = list(u)
    stack = []
    top = 0
    while u:
        c = u.pop(0)
        if c == '(':
            stack.append(c)
            top += 1
        else:
            if top == 0:
                return False
            else:
                stack.pop()
                top -= 1
    return True

def func(p):
    ## 1번 조건
    if len(p) == 0:
        return ""
    
    u, v = "", ""
    left, right = 0, 0
    
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        if p[i] == ')':
            right += 1
            
        if left >= 1 and right >= 1 and left == right:
            u = p[:i+1]
            v = p[i+1:]
            # 3번 조건 - 올바른 괄호 문자열인지 확인하는 함수
            if isCorrectString(u):
                return u + func(v)
            else:
                # 4번 조건
                new_String = "("
                new_String += func(v)
                new_String += ")"
                u = u[1:-1]

                for i in range(len(u)):
                    if u[i] == '(':
                        new_String += ')'
                    else:
                        new_String += '('
    
                return new_String

def solution(p):
    answer = ''
    
    # p 자체가 올바른 괄호 문자열 일때 (테스트 케이스 1번의 경우)
    if isCorrectString(p):
        return p
    else:
        return func(p)
    # 1번 조건
    ## 4-2의 조건을 보니 1번부터 재귀적으로 수행하므로 1번 조건도 함수로 통째로 묶었습니다.
    """
    if len(p) == 0:
        return answer
    """
    # 2번 조건
    # u와 v로 분리
    # 조건을 읽다보니 2번 조건을 재귀적으로 반복해야하는 부분이 있어서 2번조건은 함수로 빼내기로 생각
    """
    u, v = divideuv(p)
    print("함수의 결과")
    print(u, v)
    """
    ## 4번 조건이 아예 따로 된 조건이라고 생각했는데 알고보니 아니였음...
    ## 4번 조건도 함수 안에 넣어서 생각하면 될것이라고 생각하게됨
    """
    # 4번 조건
    new_String = "("
    new_u, new_v = divideuv(v)
    print("재귀를 거친 v")
    print(new_v)
    new_String += new_v
    new_String += ")"
    u = u[1:-1]
    
    for i in range(len(u)):
        if u[i] == '(':
            new_String += ')'
        else:
            new_String += '('
    """
    return answer