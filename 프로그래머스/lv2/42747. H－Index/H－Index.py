def solution(citations):
    maxci = max(citations)
    citations.sort()
    
    if maxci == 0:
        return 0
    
    for h in range(maxci, -1, -1):
        answer = 0
        
        for j in range(len(citations)-1, -1, -1):
            if h <= citations[j]:
                answer += 1
            else:
                break
        
        if h <= answer:
            answer = h
            break
        else:
            answer = 0
    return answer