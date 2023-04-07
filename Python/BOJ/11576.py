import sys
input = sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
alist = list(map(int, input().split()))
blist = []

number = 0
alist.reverse()

for i in range(len(alist)):
  number += alist[i]*A**i

while number > 0:
  blist.append(number%B)
  number //= B

blist.reverse()

print(*blist)