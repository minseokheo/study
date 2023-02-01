import sys
input = sys.stdin.readline

def gcd(a, b):
  if a > b:
    i, j = a, b
  else:
    i, j = b, a
  while i % j != 0:
    temp = j
    j = i % j
    i = temp
  
  return j

t = int(input())
res = 0

for _ in range(t):
  numbers = list(map(int, input().split()))
  for i in range(1, numbers[0]):
    for j in range(i+1, len(numbers)):
      res += gcd(numbers[i], numbers[j])
  print(res)
  res = 0