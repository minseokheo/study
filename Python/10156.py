K, N, M = map(int, input().split())

res = K * N - M

if res < 0:
  print(0)
else:
  print(res)