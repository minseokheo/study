import sys
input = sys.stdin.readline

N = int(input())

nlist = [0, 0, 1, 1]

for i in range(4, N+1):
  first_count, second_count, third_count = sys.maxsize, sys.maxsize, sys.maxsize

  if i % 3 == 0:
    first_count = nlist[i//3] + 1

  if i % 2 == 0:
    second_count = nlist[i//2] + 1
  
  third_count = nlist[i-1] + 1

  nlist.append(min(first_count, second_count, third_count))

print(nlist[N])