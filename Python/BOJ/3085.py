import sys
input = sys.stdin.readline

def check(board):
  n = len(board)
  answer = 1

  for i in range(n):
    cnt = 1

    for j in range(1, n):
      if board[i][j] == board[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      
      if cnt > answer:
        answer = cnt
    
    cnt = 1

    for j in range(1, n):
      if board[j][i] == board[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      
      if cnt > answer:
        answer = cnt
  
  return answer

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

for i in range(N):
  board[i] = list(input().rstrip())

for i in range(N):
  for j in range(N):
    if j+1 < N:
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
      temp = check(board)

      if temp > answer:
        answer = temp
      
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

    if i+1 < N:
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
      temp = check(board)

      if temp > answer:
        answer = temp
      
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)