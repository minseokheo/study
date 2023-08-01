def solution(number, k):
    answer = ''
    """
    # 문자열 슬라이싱을 통해 제일 앞 숫자를 먼저 찾아준다
    fnum = max(list(map(int, number[:k+1])))
    answer += str(fnum)
    fidx = number.index(str(fnum))  # 찾은 제일 앞 숫자의 index를 뽑아내고
    a = k - fidx    # a는 이제 k의 역할을 하게된다
    b = k + 1 # b는 남은 숫자들의 index
    
    if a == 0: # number[:k+1]에서 제일 마지막 숫자가 가장 클 경우 뒷자리를 붙이면 제일 큰 수가 된다
        answer += number[b:]
    else:
        numbers = number[fidx+1:b] # 제일 앞 숫자에서 k까지 숫자들을 모은다
        while b != len(number)-1:
            if int(numbers[0]) < int(number[b]):
                answer += number[b]
                b += 1
     """
    # 위의 방법대로 생각하니까 하다보니 모든 테스트케이스에 대해서 만족하지 못할 것으로 생각
    # 생각을 바꿔서 문자열 슬라이싱을 반복해서 제일 앞 숫자를 계속 찾아주는 방식을 택함
    a = 0
    while k != 0:
        if a+k+1 >= len(number):
            chknumber = number[a:]
            if len(chknumber) == k:
                return answer
        else:
            chknumber = number[a:a+k+1]
        maxnum = "0"
        bidx = 0
        for i in range(len(chknumber)):
            if maxnum < chknumber[i]:
                maxnum = chknumber[i]
                bidx = i
                if maxnum == '9':
                    break
        answer += maxnum
        """
        bnum = max(list(map(int, chknumber))) # 문자열 슬라이싱을 통해 answer에 들어갈 숫자를 찾아준다
        answer += str(bnum)
        """
        # bidx = chknumber.index(str(maxnum)) # 슬라이싱 된 숫자들 중에서 answer에 들어간 숫자의 index를 뽑아낸다
        k -= bidx # 뽑아낸 숫자 앞에 숫자들은 제거
        a += bidx + 1 # a는 뽑아낸 숫자 다음부터 확인해야할 index
    
    if a != len(number)-1: # 문자열 끝까지 확인 못하고 중간에 제거해야할 숫자를 다 찾으면 뒤에 덧붙여줌
        answer += number[a:]
    return answer