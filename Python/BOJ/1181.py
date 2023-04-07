N = int(input())
str_list = list()
new_list = list()

for i in range(N):
  str = input()
  str_list.append(str)

set_list = list(set(str_list))

for i in range(1, 51):
  for j in sorted(set_list):
    if len(j) == i:
      new_list.append(j)

for i in range(len(new_list)):
  if i != 0:
    if new_list[i-1] == new_list[i]:
      continue
  
  print(new_list[i])