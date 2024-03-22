def solution(participant, completion):
    answer = ""
    mar_dict = {}
    for name in participant:
        if name not in mar_dict:
            mar_dict[name] = 1
        else:
            mar_dict[name] += 1
    
    for name in completion:
        mar_dict[name] -= 1
    
    for k, v in mar_dict.items():
        if v != 0:
            answer = k
    return answer