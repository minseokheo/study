def solution(n):
    d = [0, 1, 2]
    
    if n >= 3:
        for i in range(3, n+1):
            d.append((d[i-2]+d[i-1])%1234567)
    
    return d[n]