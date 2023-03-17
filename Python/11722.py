import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1, N):
  for j in range(i):
    if A[j] > A[i]:
      dp[i] = max(dp[i], dp[j] + 1)
    else:
      dp[i] = max(dp[i], 1)

print(max(dp))