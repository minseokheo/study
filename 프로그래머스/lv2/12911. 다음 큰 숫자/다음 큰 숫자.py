def solution(n):
    answer = 0
    ncount = bin(n).count('1')
    ccount = 0
    
    b = n
    i = 0
    while ncount != ccount:
        i += 1
        c = b + i
        ccount = bin(c).count('1')
        
    answer = n + i
    
    return answer