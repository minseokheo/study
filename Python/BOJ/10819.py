from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

per = permutations(a)
ans = 0

for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j] - i[j+1])
    if s > ans:
        ans = s

print(ans)