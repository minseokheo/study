import sys
N, k = map(int, sys.stdin.readline().split())

score = [0 for i in range(N)]

score = list(map(int, sys.stdin.readline().split()))

score.sort()

print(score[-k])