def solution(N, road, K):
    
    answer = 0    
    neighbor = [[217000000 for _ in range(N+1)] for _ in range(N+1)]
    for r in road:
        neighbor[r[0]][r[1]] = min(neighbor[r[0]][r[1]], r[2])
        neighbor[r[1]][r[0]] = min(neighbor[r[0]][r[1]], r[2])    

    for k in range(N+1):
        neighbor[k][k] = 0
        for i in range(N+1):
            for j in range(N+1):
                neighbor[i][j] = min(neighbor[i][j], neighbor[i][k] + neighbor[k][j])
    
    for i in range(1, N+1):
        if neighbor[1][i] <= K:
            answer += 1
        
    return answer