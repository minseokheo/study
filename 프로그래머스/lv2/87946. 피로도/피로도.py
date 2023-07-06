from itertools import permutations

def solution(k, dungeons):
    answer = -1
    num = [i for i in range(1, len(dungeons)+1)]
    perm = list(permutations(num, len(dungeons)))
    
    for order in perm:
        current = k
        count = 0
        for o in order:
            if dungeons[o-1][0] <= current:
                current -= dungeons[o-1][1]
                count += 1
            else:
                break
        if count >= answer:
            answer = count
    return answer