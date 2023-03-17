import sys
input = sys.stdin.readline

N = int(input())
rgb = [[0 for _ in range(3)] for _ in range(N)]
answer = 2147000000

for i in range(N):
  rgb[i] = list(map(int, input().split()))

for i in range(3):
  dp = [[1001 for _ in range(3)] for _ in range(N)]
  dp[0][i] = rgb[0][i]

  for j in range(1, N):
    dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
    dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
    dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])
  
  for j in range(3):
    if i != j:
      answer = min(answer, dp[-1][j])

print(answer)