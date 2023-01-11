a, b = list(map(int, input().split()))

while a != 0 and b != 0:
  if a < b:
    if b % a == 0:
      print("factor")
    else:
      print("neither")
  elif a > b:
    if a % b == 0:
      print("multiple")
    else:
      print("neither")
  a, b = list(map(int, input().split()))