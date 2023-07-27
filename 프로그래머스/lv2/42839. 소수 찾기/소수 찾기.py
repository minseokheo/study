from itertools import permutations

global chk
chk = set()

def primenum(numtuple):
    numlist = list(numtuple)
    numstr = ''.join(s for s in numlist)
    numint = int(numstr)
    if numint == 1 or numint == 0:
        return False
    else:
        for i in range(2, numint):
            if numint % i == 0:
                return False
        if numint in chk:
            return False
        else:
            chk.add(numint)
            return True

def solution(numbers):
    answer = 0
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            result = primenum(j)
            
            if result == True:
                answer += 1
        
    return answer