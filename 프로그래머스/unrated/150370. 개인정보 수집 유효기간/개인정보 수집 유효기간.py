def solution(today, terms, privacies):
    answer = []
    termdict = {}
    year = 0
    month = 0
    date = 0
    typ = ''
    
    tyear = int(today[:4])
    tmonth = int(today[5:7])
    tday = int(today[8:10])
    
    for i in range(len(terms)):
        term = terms[i].split(" ")
        termdict[term[0]] = term[1]
    
    for i in range(len(privacies)):
        year = int(privacies[i][:4])
        month = int(privacies[i][5:7])
        day = int(privacies[i][8:10])
        typ = privacies[i][11]
                
        month += int(termdict[typ])
        day -= 1
        
        while month > 12:
            year += 1
            month -= 12
        
        if day == 0:
            month -= 1
            day = 28
            if month == 0:
                year -= 1
                month = 12
        
        if tyear > year:
            answer.append(i+1)
        elif tyear == year:
            if tmonth > month:
                answer.append(i+1)
            elif tmonth == month:
                if tday > day:
                    answer.append(i+1)
                    
    return answer