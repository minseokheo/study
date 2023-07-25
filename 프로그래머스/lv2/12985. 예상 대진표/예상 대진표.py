def solution(n,a,b):
    answer = 0
    
    while a != b:
        if a % 2 == 0:
            a //= 2
        else:
            a = (a+1) // 2

        if b % 2 == 0:
            b //= 2
        else:
            b = (b+1) // 2

        answer += 1
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer