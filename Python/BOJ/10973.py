import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if a[i-1] > a[i]:
        for j in range(N-1, 0, -1):
            if a[i-1] > a[j]:
                a[i-1], a[j] = a[j], a[i-1]
                a = a[:i] + sorted(a[i:], reverse=True)
                print(*a)
                exit()
print(-1)