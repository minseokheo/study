import sys
input = sys.stdin.readline

T = int(input())
d = [[0, 0] for _ in range(41)]
d[0] = [1, 0]
d[1] = [0, 1]
d[2] = [1, 1]

for _ in range(T):
    N = int(input())
    idx = 3
    if d[N] == [0, 0]:
        for i in range(idx, N+1):
            d[i] = [d[i-2][0] + d[i-1][0], d[i-2][1] + d[i-1][1]]
        idx = N
    print(d[N][0], d[N][1])