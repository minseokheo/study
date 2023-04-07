import sys
paper = [[0 for j in range(101)] for i in range(101)]

N = int(sys.stdin.readline())

for i in range(N):
  x, y = map(int, sys.stdin.readline().split())
  for a in range(x, x+10):
    for b in range(y, y+10):
      paper[a][b] = 1

count = 0

for i in range(101):
  for j in range(101):
    if paper[i][j] == 1:
      count += 1

print(count)