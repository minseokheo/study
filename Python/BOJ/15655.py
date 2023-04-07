import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
tmp = list()

def dfs(a):
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return
    
    for num in a:
        if num not in tmp:
            tmp.append(num)
            dfs(a[a.index(num)+1:])
            tmp.pop()


dfs(a)