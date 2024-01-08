from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    arrayA, arrayB = list(set(arrayA)), list(set(arrayB))
    # 내 생각은 
    #1 arrayA에서 최대공약수를 구하고 그 최대공약수를 이용해서 arrayB에 나눠보고 안나누어떨어지는 경우
    #2 arrayB에서 최대공약수를 구하고 그 최대공약수를 이용해서 arrayB에 나눠보고 안나누어떨어지는 경우
    # 두 경우를 모두 구하고 그 중에서 가장 큰 수를 answer로 출력하면 되지않을까?
    
    def findgcd(array):
        g = array[0]
        for i in range(1, len(array)):
            g = gcd(g, array[i])
            
        return g
    
    def checkgcd(array, gcd):
        for num in array:
            if num % gcd == 0:
                return 0
        return gcd
    
    gcdA, gcdB = findgcd(arrayA), findgcd(arrayB)
    gcdA, gcdB = checkgcd(arrayA, gcdB), checkgcd(arrayB, gcdA)
    
    if gcdA == 0 and gcdB == 0:
        return 0
    else:
        return max(gcdA, gcdB)