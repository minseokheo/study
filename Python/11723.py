import sys
input = sys.stdin.readline

M = int(input())
S = set()
change_S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

for _ in range(M):
    order = list(map(str, input().split()))

    if order[0] == "add":
        if int(order[1]) not in S:
            S.add(int(order[1]))
    elif order[0] == "remove":
        if int(order[1]) in S:
            S.remove(int(order[1]))
    elif order[0] == "check":
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        if int(order[1]) in S:
            S.remove(int(order[1]))
        else:
            S.add(int(order[1]))
    elif order[0] == "all":
        S = change_S
    elif order[0] == "empty":
        S.clear()