import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
cnt = 0
visited = [0] * (N+1)

def dfs(v):
    visited[v] = 1
    for e in graph[v]:
        if not visited[e]:
            dfs(e)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)