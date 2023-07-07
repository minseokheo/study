import math
# k진수로 바꾸는 함수
def change(n, k):
    s = []
    while n > 0:
        s.append(n % k)
        n //= k
    s.reverse()
    return s

# 소수인지 확인하는 함수
def isPrime(numlist):
    strnum = ''.join(str(s) for s in numlist)
    intnum = int(strnum)
    if intnum == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(intnum))+1):
            if intnum % i == 0:
                return False
        return True
def solution(n, k):
    answer = 0
    numbers = change(n, k) # k진수로 바꾸는 함수
    stack = []
    
    for i in range(len(numbers)):
        if numbers[i] != 0:
            stack.append(numbers[i])
        else:
            if stack:
                if isPrime(stack): # 소수인지 확인하는 함수
                    answer += 1
                stack.clear()
        if i == len(numbers)-1 and numbers[i] != 0:
            if isPrime(stack):
                answer += 1
    return answer