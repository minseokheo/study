import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nlist = list(map(int, input().split()))

for i in range(1, N):
    nlist[i] = nlist[i-1] + nlist[i]

nlist.insert(0, 0)

for _ in range(M):
    i, j = map(int, input().split())
    print(nlist[j] - nlist[i-1])