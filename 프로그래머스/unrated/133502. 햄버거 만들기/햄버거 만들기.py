def solution(ingredient):
    answer = 0
    stack = []
    
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1
    
    return answer