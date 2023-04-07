from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited_list = [0] * (N+1)
visited_list2 = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited_list[v] = 1
    print(v, end = ' ')
    for i in range(1, N+1):
        if visited_list[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited_list2[v] = 1
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in range(1, N+1):
            if visited_list2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_list2[i] = 1

dfs(V)
print()
bfs(V)