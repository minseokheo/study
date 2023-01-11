N = int(input())

rows = 100
cols = 3

miss = [[0 for j in range(cols)] for i in range(rows)]

for game in range(N):
  M = int(input())
  price = 0
  for mission in range(M):
    miss[mission][0], miss[mission][1], miss[mission][2] = list(map(int, input().split()))
  
  k, d, a = list(map(int, input().split()))

  for mission in range(M):
    m_price = k * miss[mission][0] - d * miss[mission][1] + a * miss[mission][2]
    if m_price < 0:
      continue
    else:
      price += m_price
  
  print(price)