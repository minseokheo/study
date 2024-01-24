import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

def bfs(n):
    count = 0
    q = list()
    for num in graph[n]:
        q.append(num)
    visit[n] = 1

    while q:
        a = q.pop(0)

        if visit[a] == 0:
            for num in graph[a]:
                q.append(num)
            count += 1
            visit[a] = 1

    return count
           

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))