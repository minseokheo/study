import sys
input = sys.stdin.readline

T = int(input())
d = [0 for _ in range(31)]
d[0] = 1
d[1] = 1
d[2] = 2

for _ in range(T):
    N, M = map(int, input().split())

    if d[M] == 0:
        for i in range(3, M+1):
            d[i] = d[i-1] * i
    
    print(d[M]//(d[N] * d[M-N]))