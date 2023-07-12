def solution(skill, skill_trees):
    answer = 0
    chk = 1
    
    for skills in skill_trees:
        i = 0
        for s in skills:
            if s in skill:
                if skill[i] != s:
                    chk = 0
                    break
                else:
                    i += 1
        if chk == 1:
            answer += 1
        else:
            chk = 1
    return answer