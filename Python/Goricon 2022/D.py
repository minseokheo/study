N, K, R, Q = list(map(int, input().split()))
typoon = [[0]*3]*K


for i in range(K):
  typoon[i] = list(map(int, input().split()))

for i in range(N):
  day1 = typoon[i+1][1] - typoon[i][1]
  day2 = typoon[i+1][2] - typoon[i][2]
  if day1 != 0:
    for j in range(day1-1):
      typoon.insert(i+j+1, [typoon[i+j][0]+1, typoon[i+j][1]+1, typoon[i+j][2]])
  elif day2 != 0:
    for k in range(day2-1):
      typoon.insert(i+j+1, [typoon[i+j][0]+1, typoon[i+j][1], typoon[i+j][2]+1])

print(typoon)