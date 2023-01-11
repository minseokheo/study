import sys
N, M, B = map(int, sys.stdin.readline().split())
ans = sys.maxsize
floor = 0

ground = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
  ground[i] = list(map(int, sys.stdin.readline().split()))

for target in range(257):
  maximum = 0
  minimum = 0
  for i in range(N):
    for j in range(M):
      if ground[i][j] >= target:
        maximum += ground[i][j] - target
      else:
        minimum += target - ground[i][j]
  
  if maximum + B >= minimum:
    if minimum + (maximum * 2) <= ans:
        ans = minimum + (maximum * 2)
        floor = target

print(ans, floor)