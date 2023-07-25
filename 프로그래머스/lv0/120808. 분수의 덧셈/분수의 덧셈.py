def solution(numer1, denom1, numer2, denom2):
    answer = []
    ans = []
    ans.append(numer1*denom2+numer2*denom1)
    ans.append(denom1*denom2)
    maxdiv = 1
    
    if ans[0] > ans[1]:
        for i in range(1, ans[1]+1):
            if ans[0] % i == 0 and ans[1] % i == 0:
                maxdiv = i
    elif ans[0] == ans[1]:
        ans[0] = 1
        ans[1] = 1
    else:
        for i in range(1, ans[0]+1):
            if ans[0] % i == 0 and ans[1] % i == 0:
                maxdiv = i
    ans[0] //= maxdiv
    ans[1] //= maxdiv
    
    answer = ans
    
    return answer