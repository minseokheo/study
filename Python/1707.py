import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

K = int(input())

def dfs(start, group):
    visited[start] = group

    for i in graph[start]:
        if not visited[i]:
            a = dfs(i, -group)
            if not a:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, V+1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break
    
    print("YES" if result else "NO")