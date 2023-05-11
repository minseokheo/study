import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, c_dir = map(int, input().split())
ground = list()
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 북 서 남 동
cnt = 0

for _ in range(n):
    ground.append(list(map(int, input().split())))

ground[x][y] = 1
cnt += 1

for i in range(4):
    c_dir += 1

    if c_dir > 3:
        c_dir -= 4
    
    a = x + dir[c_dir][0]
    b = y + dir[c_dir][1]

    if ground[a][b] == 0:
        x = a
        y = b
        i = 0
        cnt += 1
        ground[a][b] = 1


print(cnt)