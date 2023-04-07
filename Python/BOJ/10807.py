import sys
N = int(sys.stdin.readline())
num_list = map(int, sys.stdin.readline().split())
v = int(sys.stdin.readline())
count = 0

for num in num_list:
  if num == v:
    count += 1

print(count)