import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    now = scoville[0]

    while now < K and len(scoville) > 1:

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new = first + second*2
        answer += 1
        heapq.heappush(scoville, new)
        now = scoville[0]

    if min(scoville) < K:
        answer = -1

    return answer