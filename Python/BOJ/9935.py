import sys
input = sys.stdin.readline

s = list(input().strip())
bomb = list(input().strip())
l_bomb = len(bomb)
stack = list()

for i in s:
    stack.append(i)
    if stack[len(stack)-l_bomb:len(stack)] == bomb:
        for _ in range(l_bomb):
            stack.pop()

if stack:
    print(*stack, sep="")
else:
    print("FRULA")