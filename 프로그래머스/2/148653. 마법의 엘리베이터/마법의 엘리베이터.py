def solution(storey):
    answer = 0
    
    while storey > 0:
        num = storey % 10
        storey  = storey // 10
        if num >= 6 :
            answer = answer + (10 - num)
            storey += 1
        elif num == 5:
            if storey % 10 >= 5:
                answer = answer + (10 - num)
                storey += 1
            else:
                answer = answer + num
        else:
            answer = answer + num
    
    return answer