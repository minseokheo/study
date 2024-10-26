import sys
import heapq
input = sys.stdin.readline

N = int(input())

hq = list()

for _ in range(N):
    order = int(input())
    if order == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-heapq.heappop(hq))
    else:
        heapq.heappush(hq, -order)