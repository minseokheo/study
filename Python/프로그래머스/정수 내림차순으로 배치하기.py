def solution(n):
    n = str(n)
    answer = int(''.join(sorted(n, reverse=True)))
    return answer