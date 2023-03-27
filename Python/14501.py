import sys
input = sys.stdin.readline

N = int(input())
T = [0] * (N+1)
P = [0] * (N+1)
d = [0] * (N+2)

for i in range(N+1):
    if i == 0:
        continue
    else:
        a, b = map(int, input().split())
        T[i] = a
        P[i] = b

for i in range(N, 0, -1):
    if i + T[i] > N+1:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], P[i] + d[i + T[i]])

print(d[1])