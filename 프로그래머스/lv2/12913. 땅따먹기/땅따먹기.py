def solution(land):
    answer = 0
    score = []
    
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            for k in range(len(land[i-1])):
                if j != k:
                    score.append(land[i-1][k] + land[i][j])
            land[i][j] = max(score)
            score.clear()
    answer = max(land[-1])
    return answer