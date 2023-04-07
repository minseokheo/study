import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
d = [0 for _ in range(N)]
dlist = []

for i in range(N):
  for j in range(i):
    if A[i] > A[j] and d[i] < d[j]:
      d[i] = d[j]
  
  d[i] += 1

print(max(d))

order = max(d)

for i in range(N-1, -1, -1):
  if d[i] == order:
    dlist.append(A[i])
    order -= 1

dlist.reverse()
print(*dlist)