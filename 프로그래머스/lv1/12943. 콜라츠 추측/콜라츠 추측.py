def solution(num):
    answer = 0
    if num == 1:
        answer = 0
    else:
        i = 0
        
        while i < 500:
            if num == 1:
                break
            elif num % 2 == 0:
                num //= 2
                i += 1
            elif num % 2 == 1:
                num = num * 3 + 1
                i += 1
                
        if i == 500:
            answer = -1
        else:
            answer = i
    return answer