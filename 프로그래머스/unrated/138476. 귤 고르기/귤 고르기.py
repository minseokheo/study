def solution(k, tangerine):
    answer = 0
    tandic = {}
    for length in tangerine:
        if length not in tandic:
            tandic[length] = 1
        else:
            tandic[length] += 1
    sorted_tandic = sorted(tandic.items(), key=lambda x: x[1])
    
    for i in range(len(sorted_tandic)-1, -1, -1):
        if k-sorted_tandic[i][1] <= 0:
            answer += 1
            break
        else:
            k -= sorted_tandic[i][1]
            answer += 1
    return answer