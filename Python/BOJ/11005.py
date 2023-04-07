import sys
input = sys.stdin.readline

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
bnum = ''

while N > 0:
  bnum += str(tmp[N % B])
  N //= B

print(bnum[::-1])