def solution(n):
    answer = 1
    
    for i in range(1, n):
        j = i
        while True:
            if i == n:
                answer += 1
                break
            elif i > n:
                break
            j += 1
            i += j
    return answer