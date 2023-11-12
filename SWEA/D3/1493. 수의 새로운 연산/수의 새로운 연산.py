lst = [[0] for _ in range(100001)]
j, k = 1, 1
for i in range(1, 100001):
    lst[i] = [j, k]
    j += 1
    k -= 1
    if k == 0:
        k = j
        j = 1

T = int(input())

for test_case in range(1, T+1):
    p, q = map(int, input().split())
    sum_point = [lst[p][0] + lst[q][0], lst[p][1] + lst[q][1]]
    for i in range(1, 100001):
        if lst[i] == sum_point:
            print(f"#{test_case} {i}")
            break