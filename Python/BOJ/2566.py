import sys
matrix = [[0 for j in range(9)] for i in range(9)]

for k in range(9):
  matrix[k] = list(map(int, sys.stdin.readline().split()))

max = -1

for l in range(9):
  for m in range(9):
    if max < matrix[l][m]:
      max = matrix[l][m]
      x = l + 1
      y = m + 1 

print(max)
print(x, y)