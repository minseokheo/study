import sys
input = sys.stdin.readline

N = int(input())
a = list()

def dfs():
    if len(a) == N:
        print(*a)
        return
    
    for i in range(1, N+1):
        if i not in a:
            a.append(i)
            dfs()
            a.pop()

dfs()