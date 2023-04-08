import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

min_list = list()

for i in range(n):
    min_list.append(min(arr[i]))

print(max(min_list))