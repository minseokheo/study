import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
d = [0 for _ in range(N)]

for i in range(N):
  for j in range(i):
    if A[i] > A[j] and d[i] < d[j]:
      d[i] = d[j]
  
  d[i] += 1

print(max(d))