import heapq

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    hq = []
    ans = []
    for _ in range(N):
        order = list(map(int, input().split()))
        if order[0] == 1:
            heapq.heappush(hq, -order[1])
        elif order[0] == 2:
            if len(hq) > 0:
                ans.append(-heapq.heappop(hq))
            else:
                ans.append(-1)

    print(f"#{test_case} ", end='')
    print(*ans)