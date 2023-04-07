import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(1001)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
  dp[i][0] = 1

  for j in range(1, 10):
    dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007

print(sum(dp[N])%10007)