def dfs(numbers, cnt, target, value):
    global answer
    global visited
    if cnt == len(numbers):
        if target == value:
            answer += 1
        return
    
    if not visited[cnt]:
        visited[cnt] = 1
        dfs(numbers, cnt+1, target, value+numbers[cnt])
        dfs(numbers, cnt+1, target, value-numbers[cnt])
        visited[cnt] = 0

def solution(numbers, target):
    global answer
    answer = 0
    l = len(numbers)
    global visited
    visited = [0] * l
    value = 0
    
    dfs(numbers, 0, target, value)
    return answer