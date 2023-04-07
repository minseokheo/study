import sys
input = sys.stdin.readline

N, M = map(int, input().split())

a = []

def dfs(start):
    if len(a) == M:
      print(' '.join(map(str, a)))
      return
    
    for i in range(start, N+1):
      if i not in a:
         a.append(i)
         dfs(i+1)
         a.pop()

dfs(1)