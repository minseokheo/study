import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
first = arr[-1]
second = arr[-2]
cnt = 0
ans = 0

for i in range(M):
    if cnt >= K:
        ans += second
        cnt = 0
    else:
        ans += first
        cnt += 1

print(ans)