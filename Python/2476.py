N = int(input())

max_reward = 0

for i in range(N):
  dice_list = list(map(int, input().split()))

  if dice_list[0] == dice_list[1] == dice_list[2]:
    reward = 10000 + dice_list[0] * 1000
  elif dice_list[0] == dice_list[1] or dice_list[0] == dice_list[2]:
    reward = 1000 + dice_list[0] * 100
  elif dice_list[1] == dice_list[2]:
    reward = 1000 + dice_list[1] * 100
  else:
    reward = max(dice_list) * 100
  
  if max_reward < reward:
    max_reward = reward
  
  reward = 0

print(max_reward)