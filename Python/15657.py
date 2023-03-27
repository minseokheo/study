import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
tmp = list()

def dfs(a):
  if len(tmp) == M:
    print(' '.join(map(str, tmp)))
    return
  
  for num in a:
    if len(tmp) == 0:
      tmp.append(num)
      dfs(a)
      tmp.pop()
    elif tmp[-1] <= num:
      tmp.append(num)
      dfs(a)
      tmp.pop()


dfs(a)