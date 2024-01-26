import sys
input = sys.stdin.readline

T = int(input())
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = [(x, y)]
    ground[x][y] = 0

    while q:
        a, b = q.pop(0)

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if ground[nx][ny] == 1:
                q.append((nx, ny))
                ground[nx][ny] = 0


for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)