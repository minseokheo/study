import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))

times.sort()

answer = list()
a = 0

for time in times:
    a += time
    answer.append(a)

print(sum(answer))