def solution(genres, plays):
    answer = []
    total = dict()
    l = len(genres)
    
    for i in range(l):
        if genres[i] not in total:
            total[genres[i]] = plays[i]
        else:
            total[genres[i]] += plays[i]
    
    s_total = sorted(total.items(), key = lambda x:x[1], reverse=True)
    
    for genre, play in s_total:
        total1 = dict()
        
    
        for i in range(l):
            if genres[i] == genre:
                total1[i] = plays[i]
            if genres[i] == genre:
                total1[i] = plays[i]
    
        s_total1 = sorted(total1.items(), key=lambda x:x[1], reverse=True)
        
        cnt = 0
        for idx, p in s_total1:
            if cnt >= 2:
                continue
            answer.append(idx)
            cnt += 1
    
    return answer