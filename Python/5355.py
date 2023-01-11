num = int(input())

for i in range(num):
  cal = list(map(str, input().split()))
  result = float(cal[0])

  for j in range(1, len(cal)):
    if cal[j] == '@':
      result *= 3
    elif cal[j] == '%':
      result += 5
    elif cal[j] == '#':
      result -= 7
  
  print("{:.2f}".format(result))
