import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
visited = [False] * N
tmp = list()

def dfs():
  if len(tmp) == M:
    print(' '.join(map(str, tmp)))
    return
  elif len(tmp) == 0:
    remember = 0
    for i in range(N):
      if not visited[i] and remember != a[i]:
        visited[i] = True
        remember = a[i]
        tmp.append(a[i])
        dfs()
        visited[i] = False
        tmp.pop()
  elif len(tmp) != 0:
    remember = 0
    for i in range(N):
      if not visited[i] and remember != a[i] and tmp[-1] <= a[i]:
        visited[i] = True
        remember = a[i]
        tmp.append(a[i])
        dfs()
        visited[i] = False
        tmp.pop()

dfs()