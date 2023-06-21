def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    dir = 'r'
    
    for i in range(1, n*n+1):
        if answer[x][y] == 0:
            answer[x][y] = i

        if dir == 'r':
            y += 1
            if y == n or answer[x][y] != 0:
                dir = 'd'
                y -= 1
                x += 1
        elif dir == 'd':
            x += 1
            if x == n or answer[x][y] != 0:
                dir = 'l'
                x -= 1
                y -= 1
        elif dir == 'l':
            y -= 1
            if y == -1 or answer[x][y] != 0:
                dir = 'u'
                y += 1
                x -= 1
        elif dir == 'u':
            x -= 1
            if x == -1 or answer[x][y] != 0:
                dir = 'r'
                x += 1
                y += 1
                            
    return answer

n = int(input())
print(solution(n))