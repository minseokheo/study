import sys
input = sys.stdin.readline

n = int(input())
nlist = []

for i in range(n):
  nlist.append(list(map(int, input().split())))

k = 2
for i in range(1, n):
  for j in range(k):
    if j == 0:
      nlist[i][j] += nlist[i-1][j]
    elif i == j:
      nlist[i][j] += nlist[i-1][j-1]
    else:
      nlist[i][j] = max(nlist[i-1][j-1] + nlist[i][j], nlist[i-1][j] + nlist[i][j])

  k += 1
print(max(nlist[n-1]))