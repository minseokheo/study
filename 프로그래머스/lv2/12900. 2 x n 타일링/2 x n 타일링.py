def solution(n):
    d = [1 for _ in range(n+1)]
    if n >= 2:
        for i in range(2, n+1):
            d[i] = (d[i-1] + d[i-2]) % 1000000007
    return d[n]