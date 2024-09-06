import sys
input = sys.stdin.readline

N = int(input())
t = list()

for _ in range(N):
    t.append(list(map(int, input().split())))

t = sorted(t, key= lambda x:(x[1], x[0]))
time = 0
cnt = 0

for i in range(len(t)):
    if i == 0:
        time = t[i][1]
        cnt += 1
    else:
        if time <= t[i][0]:
            time = t[i][1]
            cnt += 1

print(cnt)