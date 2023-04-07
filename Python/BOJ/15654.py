import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
tmp = list()

def dfs():
  if len(tmp) == M:
    print(' '.join(map(str, tmp)))
    return
  
  for num in a:
    if num not in tmp:
      tmp.append(num)
      dfs()
      tmp.pop()

dfs()