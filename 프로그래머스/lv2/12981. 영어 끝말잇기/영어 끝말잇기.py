def solution(n, words):
    answer = []
    chkwords = []
    for i in range(len(words)):
        if i != 0:
            if words[i-1][-1] != words[i][0]:
                answer.append(i%n+1)
                answer.append(i//n+1)
                break
            elif words[i] in chkwords:
                answer.append(i%n+1)
                answer.append(i//n+1)
                break                              
        chkwords.append(words[i])
                            
    if len(answer) == 0:
        answer.append(0)
        answer.append(0)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer