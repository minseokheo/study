dish = list(input())

height = 0

for i in range(len(dish)):
  if i == 0:
    height += 10
    continue
  
  if dish[i-1] == dish[i]:
    height += 5
  else:
    height += 10

print(height)