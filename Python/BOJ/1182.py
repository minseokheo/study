import sys
input = sys.stdin.readline

N, S = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
tmp = list()

def back_tracking(start):
    global cnt
    if sum(tmp) == S and len(tmp) > 0:
        cnt += 1

    for i in range(start, N):
        tmp.append(a[i])
        back_tracking(i+1)
        tmp.pop()

back_tracking(0)
print(cnt)