import sys
input = sys.stdin.readline

N = int(input())
shirt = list(map(int, input().split()))
T, P = map(int, input().split())
cnt = 0

for s in shirt:
    cnt += s//T
    if s%T != 0:
        cnt += 1

print(cnt)
print(N//P,N%P)