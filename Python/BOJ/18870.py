import sys
N = int(sys.stdin.readline())

point =  [0 for i in range(N)]
point = list(map(int, sys.stdin.readline().split()))
result = list()

s_point = set(point)
result = list(s_point)
result.sort()

numdict = {}

for i in range(len(result)):
  numdict[result[i]] = i

for value in point:
  print(numdict[value], end = " ")