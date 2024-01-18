import sys
input = sys.stdin.readline

N, M = map(int, input().split())
names = dict()
not_heard = list()
not_heard_and_seen = list()

for _ in range(N+M):
    name = input().rstrip()
    if name not in names:
        names[name] = 1
    else:
        not_heard_and_seen.append(name)

# for _ in range(N):
#     not_heard.append(input().rstrip())

# for _ in range(M):
#     name = input().rstrip()
#     if name in not_heard:
#         not_heard_and_seen.append(name)

not_heard_and_seen.sort()

print(len(not_heard_and_seen))

for name in not_heard_and_seen:
    print(name)