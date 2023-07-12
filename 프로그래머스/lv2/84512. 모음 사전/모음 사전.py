def solution(word):
    answer = 0
    dic = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U'}
    w = ""
    d = {}
    while w != "UUUUU":
        answer += 1
        
        if len(w) < 5:
            w += 'A'
        elif len(w) == 5:
            if w[4] != 'U':
                w = w[0:4] + dic[w[4]]
            else:
                if w[3] == 'U':
                    if w[2] == 'U':
                        if w[1] == 'U':
                            w = dic[w[0]]
                        else:
                            w = w[0] + dic[w[1]]
                    else:
                        w = w[0:2] + dic[w[2]]
                else:
                    w = w[0:3] + dic[w[3]]
        d[w] = answer
    return d[word]