def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    f, s, t = 0, 0, 0
    f_i, s_i, t_i = 0, 0, 0
    
    for a in answers:
        if a == first[f_i]:
            f += 1
        if a == second[s_i]:
            s += 1
        if a == third[t_i]:
            t += 1
        f_i += 1
        s_i += 1
        t_i += 1
        
        if f_i >= 5:
            f_i = 0
        if s_i >= 8:
            s_i = 0
        if t_i >= 10:
            t_i = 0
    
    score = [f, s, t]
    ms = max(score)
    for i in range(len(score)):
        if ms == score[i]:
            answer.append(i+1)
    
    return answer