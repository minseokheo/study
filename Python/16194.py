import sys
input = sys.stdin.readline

N = int(input())
price = list(map(int, input().split()))
d = [0 for _ in range(N+1)]
d[1] = price[0]

for i in range(2, N+1):
  min_price = price[i-1]

  for j in range(1, i//2+1):
    min_price = min(min_price, d[i-j]+d[j])
  
  d[i] = min_price

print(d[N])