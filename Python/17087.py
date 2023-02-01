import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

def gcd(a, b=0):
  if b == 0:
    return a
  
  if b > a:
    temp = a
    a = b
    b = temp
  
  while b > 0:
    temp = b
    b = a%b
    a = temp
  
  return a

def many_gcd(numbers):
  res = 0

  for i in range(len(numbers)):
    res = gcd(numbers[i], res)
  
  return res

for i in range(len(A)):
  if A[i] > S:
    A[i] -= S
  else:
    A[i] = S - A[i]

print(many_gcd(A))