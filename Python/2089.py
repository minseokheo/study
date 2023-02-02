import sys
input = sys.stdin.readline

N = int(input())
minbin = ""
if N == 0:
  print(0)

while N != 0:
  a = N%-2
  b = N//-2

  if a < 0:
    minbin = "1" + minbin
    b += 1
  else:
    minbin = "0" + minbin

  N = b

print(minbin)