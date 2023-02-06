import sys
input = sys.stdin.readline

n = int(input())
d = [1, 1]

for i in range(2, n+1):
  d.append((d[i-1] + 2*d[i-2])%10007)

print(d[n])