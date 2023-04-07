dice_list = list(map(int, input().split()))

temp = 0

if dice_list[0] == dice_list[1]:
  temp = 1
  if dice_list[0] == dice_list[2]:
    temp = 4
elif dice_list[1] == dice_list[2]:
  temp = 2
elif dice_list[0] == dice_list[2]:
  temp = 3

if temp == 0:
  print(max(dice_list) * 100)
elif temp == 1:
  print(1000 + dice_list[0] * 100)
elif temp == 2:
  print(1000 + dice_list[1] * 100)
elif temp == 3:
  print(1000 + dice_list[2] * 100)
elif temp == 4:
  print(10000 + dice_list[0] * 1000)