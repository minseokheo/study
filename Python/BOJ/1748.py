import sys
input = sys.stdin.readline

N = int(input())
digits = len(str(N))
ans = 0

for i in range(digits, 0, -1):
  if i == digits:
    ans = (N - (10**(i-1)-1))*i
  else:
    ans += ((10**i-1) - (10**(i-1)-1))*i

print(ans)