def solution(priorities, location):
    answer = 0
    i = 0
    l = len(priorities)
    ready = 1
    chk = 0
    
    while priorities[i]:
        for j in range(i+1, len(priorities)):
            if priorities[i] < priorities[j]:
                priorities.append(priorities[i])
                priorities[i] = 0
                chk = 1
                break
        if chk == 1:
            chk = 0
        else:
            priorities[i] = 0
            if i % l == location:
                return ready
            priorities.append(-1)
            ready += 1
        i += 1        
                
    return answer