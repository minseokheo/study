import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poketmon = dict()
idx = 1

for _ in range(N):
    name = input().rstrip()
    poketmon[name] = idx
    poketmon[idx] = name
    idx += 1

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(poketmon[int(question)])
    else:
        print(poketmon[question])