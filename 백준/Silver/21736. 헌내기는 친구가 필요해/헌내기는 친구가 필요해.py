import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

campus = list()
v = [[True for _ in range(M)] for _ in range(N)]

for _ in range(N):
    campus.append(list(input().rstrip()))

start = list()

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start = [i, j]
        if campus[i][j] == 'X':
            v[i][j] = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([start])
p = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and v[nx][ny] and campus[nx][ny] != 'X':
            queue.append([nx, ny])
            v[nx][ny] = False

            if campus[nx][ny] == 'P':
                p += 1

if p == 0:
    print("TT")
else:
    print(p)