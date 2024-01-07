def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def solution(n, k):
    answer = []
    nlist = [i for i in range(1, n+1)]
    
    while n > 1:
        facto = factorial(n-1)
        if k % facto == 0:
            answer.append(nlist[int(k//facto)-1])
            nlist.remove(nlist[int(k//facto)-1])
            k = facto
        else:
            answer.append(nlist[int(k//facto)])
            nlist.remove(nlist[int(k//facto)])
            k = k % facto
        n -= 1
    
    answer.append(nlist[0])
    
    return answer