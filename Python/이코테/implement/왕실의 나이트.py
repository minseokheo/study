import sys
input = sys.stdin.readline

loc = input()
result = 0

col = int(ord(loc[0])) - int(ord('a'))
row = int(loc[1]) - 1
steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

for step in steps:
    x = row + step[0]
    y = col + step[1]
    if x < 0 or y < 0 or x > 7 or y > 7:
        continue
    result += 1

print(result)