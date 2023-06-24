def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = 0, 0, 0, 0
    luxchk = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if luxchk == 0:
                    lux = i
                    luy = j
                    rdx = i+1
                    rdy = j+1
                    luxchk = 1
                    continue
                
                if luy > j:
                    luy = j
                
                rdx = i+1
                
                if rdy < j+1:
                    rdy = j+1
                print(lux, luy, rdx, rdy)
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)
    return answer