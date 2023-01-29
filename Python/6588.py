import sys
import math
input = sys.stdin.readline

n = 1000000
prime_chk = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
  if prime_chk[i] == True:
    j = 2
    while i * j <= n:
      prime_chk[i*j] = False
      j += 1

n = int(input())

while n != 0:
  for a in range(3, n, 2):
    b = n-a
    if prime_chk[a] == True and prime_chk[b] == True:
      print("{} = {} + {}".format(n, a, b))
      break
    if a == n-1:
      print("Goldbach's conjecture is wrong.")
  n = int(input())