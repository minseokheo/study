from collections import deque

def solution(m, n, board):
    answer = 0
    chkboard = [[1 for _ in range(n)] for _ in range(m)]
    chk = 0
    listboard = []
    
    for i in range(m):
        listboard.append(list(board[i]))

    while True:
        for i in range(m-1):
            for j in range(n-1):
                if listboard[i][j] != 0 and listboard[i][j] == listboard[i][j+1] and listboard[i][j+1] == listboard[i+1][j] and listboard[i+1][j] == listboard[i+1][j+1]:
                    chkboard[i][j], chkboard[i][j+1], chkboard[i+1][j], chkboard[i+1][j+1] = 2, 2, 2, 2
                    chk = 1
        if chk == 0:
            break
        else:
            chk = 0
            for i in range(m):
                for j in range(n):
                    if chkboard[i][j] == 2:
                        answer += 1
        
        for i in range(n):
            queue = deque()
            for j in range(m-1, -1, -1):
                if chkboard[j][i] == 2 or chkboard[j][i] == 0:
                    queue.append([j, i])
                    listboard[j][i] = 0
                    chkboard[j][i] = 0
                if queue and chkboard[j][i] == 1:
                    x, y = queue.popleft()
                    chkboard[x][y], chkboard[j][i] = chkboard[j][i], chkboard[x][y]
                    listboard[x][y], listboard[j][i] = listboard[j][i], listboard[x][y]
                    queue.append([j, i])
    return answer