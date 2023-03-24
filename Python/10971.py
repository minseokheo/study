import sys
input = sys.stdin.readline

N = int(input())
a = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    a[i] = list(map(int, input().split()))
ans = sys.maxsize
visited = [0] * N

def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return
    if value > ans:
        return
    
    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)