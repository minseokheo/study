import sys
check = [0 for i in range(31)]

for j in range(28):
  n = int(sys.stdin.readline())
  check[n] = 1

for k in range(1, 31):
  if check[k] == 0:
    print(k)