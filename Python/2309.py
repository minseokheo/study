import sys
input = sys.stdin.readline

height = []
fake = 0
find = 0

for i in range(9):
  height.append(int(input()))
  fake += height[i]

height.sort()
seek = fake - 100

for i in range(8):
  for j in range(i+1, 9):
    if height[i] + height[j] == seek:
      height.remove(height[j])
      height.remove(height[i])
      find = 1
      break
  if find == 1:
    break

for i in range(7):
  print(height[i])