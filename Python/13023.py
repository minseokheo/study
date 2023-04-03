import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rela = [[]for _ in range(N)]
visited = [False] * 2001
ans = False

for _ in range(M):
    a, b = map(int, input().split())
    rela[a].append(b)
    rela[b].append(a)

def dfs(idx, depth):
    global ans
    visited[idx] = True

    if depth == 4:
        ans = True
        return
    
    for i in rela[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth+1)
            visited[i] = False

for i in range(N):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

if ans:
    print(1)
else:
    print(0)