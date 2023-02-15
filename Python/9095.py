import sys
input = sys.stdin.readline

T = int(input())
d = [0, 1, 2, 4]

for i in range(4, 11):
  d.append(d[i-1]+d[i-2]+d[i-3])


for _ in range(T):
  n = int(input())
  print(d[n])