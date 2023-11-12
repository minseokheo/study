T = int(input())
for test_case in range(1, T+1):
    H, W = map(int, input().split())
    m = list()
    for _ in range(H):
        m.append(list(input()))
    N = int(input())
    for i in range(H):
        for j in range(W):
            if m[i][j] == '^':
                pos = [i, j, 0]
            elif m[i][j] == '>':
                pos = [i, j, 1]
            elif m[i][j] == 'v':
                pos = [i, j, 2]
            elif m[i][j] == '<':
                pos = [i, j, 3]

    order_list = list(input())
    for order in order_list:
        if order == 'U':
            pos[2] = 0
            if pos[0] > 0 and m[pos[0]-1][pos[1]] == '.':
                m[pos[0]][pos[1]] = '.'
                pos[0] -= 1
            m[pos[0]][pos[1]] = '^'
        elif order == 'D':
            pos[2] = 2
            if pos[0] < H-1 and m[pos[0]+1][pos[1]] == '.':
                m[pos[0]][pos[1]] = '.'
                pos[0] += 1
            m[pos[0]][pos[1]] = 'v'
        elif order == 'L':
            pos[2] = 3
            if pos[1] > 0 and m[pos[0]][pos[1]-1] == '.':
                m[pos[0]][pos[1]] = '.'
                pos[1] -= 1
            m[pos[0]][pos[1]] = '<'
        elif order == 'R':
            pos[2] = 1
            if pos[1] < W-1 and m[pos[0]][pos[1]+1] == '.':
                m[pos[0]][pos[1]] = '.'
                pos[1] += 1
            m[pos[0]][pos[1]] = '>'
        elif order == 'S':
            if pos[2] == 0:
                for x in range(pos[0]-1, -1, -1):
                    if m[x][pos[1]] == '*':
                        m[x][pos[1]] = '.'
                        break
                    elif m[x][pos[1]] == '#':
                        break
            elif pos[2] == 1:
                for y in range(pos[1]+1, W):
                    if m[pos[0]][y] == '*':
                        m[pos[0]][y] = '.'
                        break
                    elif m[pos[0]][y] == '#':
                        break
            elif pos[2] == 2:
                for x in range(pos[0]+1, H):
                    if m[x][pos[1]] == '*':
                        m[x][pos[1]] = '.'
                        break
                    elif m[x][pos[1]] == '#':
                        break
            elif pos[2] == 3:
                for y in range(pos[1]-1, -1, -1):
                    if m[pos[0]][y] == '*':
                        m[pos[0]][y] = '.'
                        break
                    elif m[pos[0]][y] == '#':
                        break
    print(f"#{test_case} ", end='')
    for i in range(H):
        print(''.join(m[i]))