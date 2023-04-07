import sys
input = sys.stdin.readline

N = int(input())
cost = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
  cost[i] = list(map(int, input().split()))


for i in range(1, N):
  cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
  cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
  cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))