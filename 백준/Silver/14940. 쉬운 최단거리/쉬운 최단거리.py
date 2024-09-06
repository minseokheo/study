import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
zido = list()
visited = [[0 for _ in range(m)] for _ in range(n)]
answer = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    zido.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if zido[i][j] == 2:
            x, y = i, j

q = deque()
q.append([x, y])
visited[x][y] = 1
direct = [[0, -1], [0, 1], [-1, 0], [1, 0]] # 좌 우 상 하

while q:
    x, y = q.popleft()
    
    for d in direct:
        dx = x + d[0]
        dy = y + d[1]
        if 0 <= dx < n and 0 <= dy < m:
            if zido[dx][dy] != 0 and visited[dx][dy] == 0:
                answer[dx][dy] = answer[x][y] + 1
                visited[dx][dy] = 1
                q.append([dx, dy])


for i in range(n):
    for j in range(m):
        if answer[i][j] == 0 and zido[i][j] == 2:
            print(answer[i][j], end=' ')
        elif answer[i][j] == 0 and zido[i][j] != 0:
            print(-1, end=' ')
        else:
            print(answer[i][j], end=' ')
    print()