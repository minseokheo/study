T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_list = list()
    for num in num_list:
        append_list = list()
        for sum_num in sum_list:
            append_list.append(sum_num + num)
        sum_list = sum_list + append_list
        sum_list.append(num)
    ans = sum_list.count(K)
    print(f"#{test_case} {ans}")