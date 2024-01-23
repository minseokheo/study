import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pass_dict = dict()

for _ in range(N):
    add, password = map(str, input().split())
    pass_dict[add] = password

for _ in range(M):
    find_add = input().rstrip()
    print(pass_dict[find_add])