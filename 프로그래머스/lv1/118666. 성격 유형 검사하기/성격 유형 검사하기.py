def solution(survey, choices):
    answer = ''
    sdict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        if choices[i] > 4:
            sdict[survey[i][1]] += (choices[i] - 4)
        elif choices[i] < 4:
            sdict[survey[i][0]] += (4 - choices[i])
        
        print(sdict)
    
    if sdict['R'] >= sdict['T']:
        answer += 'R'
    elif sdict['R'] < sdict['T']:
        answer += 'T'
        
    if sdict['C'] >= sdict['F']:
        answer += 'C'
    elif sdict['C'] < sdict['F']:
        answer += 'F'
        
    if sdict['J'] >= sdict['M']:
        answer += 'J'
    elif sdict['J'] < sdict['M']:
        answer += 'M'
        
    if sdict['A'] >= sdict['N']:
        answer += 'A'
    elif sdict['A'] < sdict['N']:
        answer += 'N'
        
    return answer