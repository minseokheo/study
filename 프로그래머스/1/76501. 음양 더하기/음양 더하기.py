def solution(absolutes, signs):
    answer = 0
    
    l = len(absolutes)
    
    for i in range(l):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer