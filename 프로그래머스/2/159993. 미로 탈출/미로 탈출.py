from collections import deque
def bfs(s, e, maps):
    #상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    r = len(maps)
    c = len(maps[0])
    v = [[False]*c for _ in range(r)]
    q = deque()
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] == s:
                q.append((i, j, 0))
                v[i][j] = True
                break
        if q:
            break
            
    while q:
        y, x, cost = q.popleft()
        
        if maps[y][x] == e:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny<r and 0<=nx<c and maps[ny][nx] != 'X':
                if not v[ny][nx]:
                    q.append((ny, nx, cost+1))
                    v[ny][nx] = True
    
    return -1
    
    
def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)
    
    if path1 != -1 and path2 != -1:
        return path1 + path2
    else:
        return -1