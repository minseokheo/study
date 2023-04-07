import sys
input = sys.stdin.readline

N = int(input())
price = list(map(int, input().split()))
d = [0 for _ in range(N+1)]
d[1] = price[0]

for i in range(1, N):
  max = price[i]

  for j in range(i+1, i//2, -1):
    if max <= d[j-1] + d[(i+1)-(j-1)]:
      max = d[j-1] + d[((i+1) - (j-1))]
  
  d[i+1] = max
print(d[N])