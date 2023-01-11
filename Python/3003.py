chess = list(map(int, input().split()))
a = [1, 1, 2, 2, 2, 8]

for i in range(len(a)):
  print(a[i] - chess[i], end = ' ')