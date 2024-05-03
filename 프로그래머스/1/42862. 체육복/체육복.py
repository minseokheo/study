def solution(n, lost, reserve):
    answer = 0
    clothes = [1 for _ in range(n)]
    
    for l in lost:
        clothes[l-1] -= 1
    
    for r in reserve:
        clothes[r-1] += 1
        
    for i in range(n):
        if clothes[i] == 0:
            if i-1 > -1:
                if clothes[i-1] > 1:
                    clothes[i-1] -= 1
                    clothes[i] += 1
                    continue
            if i+1 < n:
                if clothes[i+1] > 1:
                    clothes[i+1] -= 1
                    clothes[i] += 1
                    continue
    
    for cloth in clothes:
        if cloth > 0:
            answer += 1
            
    return answer