import sys
input = sys.stdin.readline

N = int(input())
st = [0 for _ in range(301)]
d = [0 for _ in range(301)]

for i in range(N):
    st[i] = int(input())

d[0] = st[0]
d[1] = max(st[0] + st[1], st[1])
d[2] = max(st[0] + st[2], st[1] + st[2])

if N < 3:
    print(d[N-1])
else:
    for i in range(3, N):
        d[i] = max(d[i-3] + st[i-1] + st[i], d[i-2] + st[i])
    print(d[N-1])