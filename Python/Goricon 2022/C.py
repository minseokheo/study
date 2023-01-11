N = int(input())
count = 0

if N == 1:
  print(1)
else:
  domino = [[0]*2]*(N+1)
  ch_domino = [1]*(N+1)

  for i in range(N):
    domino[i] = list(map(int, input().split()))

  for j in range(N):
    if ch_domino[j] == 1:
      ch_domino[j] = 0
      count += 1
    if domino[j+1]:
      if domino[j][0] + domino[j][1] >= domino[j+1][0]:
        ch_domino[j+1] = 0
  print(count)