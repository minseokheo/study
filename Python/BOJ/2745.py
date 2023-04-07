import sys
input = sys.stdin.readline

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
res = 0

for i in range(len(N)-1, -1, -1):
  res += int(tmp.index(N[i])) * int(B) ** (len(N)-i-1)

print(res)