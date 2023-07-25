from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    l = len(q1) + len(q2)
    sq1 = sum(queue1)
    sq2 = sum(queue2)
    
    if (sq1+sq2) % 2 == 1:
        return -1
    
    while sq1 != sq2:
        if answer >= l:
            return -1
        while q2 and sq1 > sq2:
            x = q1.popleft()
            q2.append(x)
            sq1 -= x
            sq2 += x
            answer += 1
        while q1 and sq1 < sq2:
            x = q2.popleft()
            q1.append(x)
            sq2 -= x
            sq1 += x
            answer += 1
    return answer