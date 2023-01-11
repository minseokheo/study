grade = list(input())

num = 0

if grade[0] == 'A':
  num = 4.0
  if grade[1] == '+':
    num += 0.3
  elif grade[1] == '-':
    num -= 0.3
elif grade[0] == 'B':
  num = 3.0
  if grade[1] == '+':
    num += 0.3
  elif grade[1] == '-':
    num -= 0.3
elif grade[0] == 'C':
  num = 2.0
  if grade[1] == '+':
    num += 0.3
  elif grade[1] == '-':
    num -= 0.3
elif grade[0] == 'D':
  num = 1.0
  if grade[1] == '+':
    num += 0.3
  elif grade[1] == '-':
    num -= 0.3
else:
  num = 0.0

print(num)