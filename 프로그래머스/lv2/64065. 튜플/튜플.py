def solution(s):
    answer = []
    numdict = {}
    numstack = ''
    sort_dict = {}
    
    for i in range(len(s)-1):
        if s[i].isdigit():
            numstack += s[i]
        elif s[i] =='}' or s[i] == ',':
            if numstack:
                if int(numstack) not in numdict:
                    numdict[int(numstack)] = 1
                else:
                    numdict[int(numstack)] += 1
                numstack = ''
    answer = sorted(numdict, key = lambda x : numdict[x], reverse = True)
    return answer