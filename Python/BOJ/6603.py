import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
tmp = list()

def dfs():
    if len(tmp) == 6:
        print(*tmp)
        return
    
    for i in s:
        if len(tmp) == 0:
            tmp.append(i)
            dfs()
            tmp.pop()
        elif i not in tmp and tmp[-1] < i:
            tmp.append(i)
            dfs()
            tmp.pop()

while a[0] != 0:
    s = a[1:]
    dfs()
    print()
    a = list(map(int, input().split()))