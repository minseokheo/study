import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = sorted(list(map(int, input().split())))
tmp  = list()

def dfs():
  if len(tmp) == M:
    print(*tmp)
    return
  remember = 0
  for num in a:
    if remember != num:
      tmp.append(num)
      remember = num
      dfs()
      tmp.pop()

dfs()