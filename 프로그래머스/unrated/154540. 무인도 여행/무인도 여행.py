# 처음 생각해낸 방법은 미로문제를 해결하듯이 새로운 이차원배열을 만들어서 연결되는 무인도는 dfs나 bfs를 활용해서 푸는 방법을 생각했습니다.
from collections import deque

def dfs(maps, chk, i, j, h, w):
    need_visited = deque()
    res = 0
    need_visited.append([i, j])
    
    while need_visited:
        x, y = need_visited.pop()
        
        if chk[x][y] == 0:
            res += int(maps[x][y])
            chk[x][y] = 1
            # 상
            if x > 0 and chk[x-1][y] == 0:
                need_visited.append([x-1, y])
            # 하
            if x < h-1 and chk[x+1][y] == 0:
                need_visited.append([x+1, y])
            # 좌
            if y > 0 and chk[x][y-1] == 0:
                need_visited.append([x, y-1])
            # 우
            if y < w-1 and chk[x][y+1] == 0:
                need_visited.append([x, y+1])
                
    return res
        
def solution(maps):
    answer = []
    height = len(maps)
    width = len(maps[0])
    chk = [[0 for i in range(width)] for j in range(height)]
    
    # chk 리스트를 만들어서 X부분인 곳은 1로 표시(갈 수 있는 곳은 모두 0)
    for i in range(height):
        for j in range(width):
            if maps[i][j] == 'X':
                chk[i][j] = 1
    
    # 0이 발견되면 dfs를 돌려서 식량 출력
    for i in range(height):
        for j in range(width):
            if chk[i][j] == 0:
                answer.append(dfs(maps, chk, i, j, height, width))
    
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer