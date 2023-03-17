import sys
input = sys.stdin.readline

n = int(input())
grape = list()
dp = list()

for i in range(n):
  grape.append(int(input()))

  if i == 0:
    dp.append(grape[0])
  elif i == 1:
    dp.append(grape[0]+grape[1])
  elif i == 2:
    dp.append(max(grape[0]+grape[1], grape[1]+grape[2], grape[0]+grape[2]))
  else:
    dp.append(max(dp[i-1], dp[i-2] + grape[i], dp[i-3] + grape[i-1] + grape[i]))

print(dp[n-1])