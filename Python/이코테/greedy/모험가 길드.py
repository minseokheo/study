import sys
input = sys.stdin.readline

N = int(input())
scared = list(map(int, input().split()))
scared.sort()

group_count = 0
ingroup = 0

for data in scared:
    ingroup += 1
    if ingroup == data:
        group_count += 1
        ingroup = 0

print(group_count)