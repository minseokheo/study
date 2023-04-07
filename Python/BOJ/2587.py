import sys
num = list()
sum = 0

for i in range(5):
  n = int(sys.stdin.readline())
  num.append(n)
  sum += n

print(sum//5)

num.sort()

print(num[2])