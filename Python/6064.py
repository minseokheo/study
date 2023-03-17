import sys
input = sys.stdin.readline

def cal(m, n, x, y):
  k = x
  while k <= m * n:
    if (k - x) % m == 0 and (k - y) % n == 0:
      return k
    k += M
  return -1

T = int(input())

for _ in range(T):
  M, N, x, y = map(int, input().split())
  print(cal(M, N, x, y))