import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(2)]
dp[0][0] = nlist[0]
dp[1][0] = -1001

for i in range(1, n):
  dp[0][i] = max(dp[0][i-1]+nlist[i], nlist[i])
  dp[1][i] = max(dp[0][i-1], dp[1][i-1]+nlist[i])

print(max(max(dp[0]), max(dp[1])))