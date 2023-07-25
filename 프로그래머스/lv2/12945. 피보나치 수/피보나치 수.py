def solution(n):
    answer = 0
    pib = [0, 1]
    for i in range(2, n+1):
        pib.append(pib[i-1] + pib[i-2])
    
    answer = pib[n] % 1234567
    return answer