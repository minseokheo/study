N, M, q = list(map(int, input().split()))

rows = N
cols = M
arr = [[0]*cols]*rows
query = list()
temp = list()

for rows in range(N):
  arr[rows] = list(map(int, input().split()))

for k in range(q):
  query = list(map(int, input().split()))

  if query[0] == 0:
    arr[query[1]][query[2]] = query[3]
  elif query[0] == 1:
    temp = arr[query[1]]
    arr[query[1]] = arr[query[2]]
    arr[query[2]] = temp

for rows in range(N):
  print(*arr[rows])