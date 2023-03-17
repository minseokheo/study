import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = []

def dfs():
  if len(a) == M:
    print(' '.join(map(str, a)))
    return
  
  for i in range(1, N+1):
    if len(a) == 0:
      a.append(i)
      dfs()
      a.pop()
    elif a[-1] <= i:
      a.append(i)
      dfs()
      a.pop()

dfs()