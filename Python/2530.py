A, B, C = map(int, input().split())
D = int(input())

sec = D % 60
min = (D // 60) % 60
hour = D // 60 // 60

C += sec
B += min
A += hour

if C >= 60:
  C -= 60
  B += 1

if B >= 60:
  B -= 60
  A += 1

while A >= 24:
  A -= 24

print("{} {} {}".format(A, B, C))