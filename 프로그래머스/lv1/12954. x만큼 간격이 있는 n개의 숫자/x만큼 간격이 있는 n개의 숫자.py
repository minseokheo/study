def solution(x, n):
    answer = []
    a = x
    for _ in range(n):
        answer.append(a)
        a += x
    return answer