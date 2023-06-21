def solution(dots):
    answer = 0
    
    diff1 = (dots[1][1]-dots[0][1])/(dots[1][0]-dots[0][0])
    diff2 = (dots[3][1]-dots[2][1])/(dots[3][0]-dots[2][0])
    
    if diff1 == diff2:
        answer = 1
    
    diff1 = (dots[2][1]-dots[0][1])/(dots[2][0]-dots[0][0])
    diff2 = (dots[3][1]-dots[1][1])/(dots[3][0]-dots[1][0])
    
    if answer == 0:
        if diff1 == diff2:
            answer = 1
    
    diff1 = (dots[3][1]-dots[0][1])/(dots[3][0]-dots[0][0])
    diff2 = (dots[2][1]-dots[1][1])/(dots[2][0]-dots[1][0])
    
    if answer == 0:
        if diff1 == diff2:
            answer = 1
        
        
    return answer