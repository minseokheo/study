import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = list()

for _ in range(N):
    tomato.append(list(map(int, input().split())))

start = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            start.append([i, j, 0])

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

while start:
    x, y, t = start.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            start.append([nx, ny, t+1])

chk = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            chk = 1
            break
    if chk == 1:
        break

if chk == 0:
    print(t)