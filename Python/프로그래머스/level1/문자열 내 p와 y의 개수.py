def solution(s):
    answer = True
    pcount = 0
    ycount = 0
    
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pcount += 1
        elif s[i] == 'y' or s[i] == 'Y':
            ycount += 1
    
    if pcount != ycount:
        answer = False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(answer)

    return answer