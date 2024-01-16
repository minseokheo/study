import sys
input = sys.stdin.readline

p = [0 for _ in range(101)]
p[0] = 1
p[1] = 1
p[2] = 1

T = int(input())

for _ in range(T):
    N = int(input())

    for i in range(3, N):
        p[i] = p[i-3] + p[i-2]

    print(p[N-1])