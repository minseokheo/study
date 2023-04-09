import sys
input = sys.stdin.readline

n = int(input())
plan = list(map(str, input().split()))
x, y = 1, 1

for move in plan:
    if move == 'L':
        if x != 1:
            x -= 1
    elif move == 'R':
        if x != n:
            x += 1
    elif move == 'U':
        if y != 1:
            y -= 1
    elif move == 'D':
        if y != n:
            y += 1

print(y, x)