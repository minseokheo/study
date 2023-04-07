a, b = map(int, input().split())

while a != 0 and b != 0:
  if a <= b:
    print("No")
  else:
    print("Yes")

  a, b = map(int, input().split())