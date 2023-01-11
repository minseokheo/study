import sys

N, M = map(int, sys.stdin.readline().split())
matrixA = [[0 for j in range(M)] for i in range(N)]
matrixB = [[0 for l in range(M)] for k in range(N)]

for m in range(N):
  matrixA[m] = list(map(int, sys.stdin.readline().split()))

for n in range(N):
  matrixB[n] = list(map(int, sys.stdin.readline().split()))

for o in range(N):
  for p in range(M):
    print(matrixA[o][p] + matrixB[o][p], end = " ")
  print()