T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    sum_data = N + M
    str1_list = list(input().split())
    str2_list = list(input().split())

    sum_list_data = str1_list + str2_list
    ans = sum_data - len(set(sum_list_data))

    print(f"#{test_case} {ans}")