def solution(want, number, discount):
    answer = 0
    wants = []
    
    for w, n in zip(want, number):
        wants += [w] * n
    
    wants.sort()
    
    for i in range(len(discount)-9):
        answer += (wants == sorted(discount[i:i+10]))
    
    return answer