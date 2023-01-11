A, B = map(int, input().split())
C = int(input())

hour = C // 60
min = C % 60

if B + min >= 60:
  B = (B + min) % 60
  A += 1
else:
  B = B + min

A += hour

if A >= 24:
  A -= 24

print(A, B)