T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time.sort()
    making_time = 0
    bread = 0
    chk = 0
    for t in arrive_time:
        while making_time + M <= t:
            making_time += M
            bread += K
        if bread == 0:
            print(f"#{test_case} Impossible")
            chk = 1
            break
        else:
            bread -= 1
    if chk == 0:
        print(f"#{test_case} Possible")