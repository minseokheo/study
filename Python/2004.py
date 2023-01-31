import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def two_count(a):
  two = 0

  while a != 0:
    a = a // 2
    two += a
  
  return two

def five_count(b):
  five = 0
  
  while b != 0:
    b = b // 5
    five += b

  return five

print(min(two_count(n) - two_count(n-m) - two_count(m), five_count(n) - five_count(n-m) - five_count(m)))