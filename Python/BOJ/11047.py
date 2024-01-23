import sys
input = sys.stdin.readline

N, K = map(int, input().split())
values = list()
answer = 0

for _ in range(N):
    values.append(int(input()))

for i in range(len(values)-1, -1, -1):
    if K >= values[i]:
        answer += K // values[i]
        K = K % values[i]

print(answer)