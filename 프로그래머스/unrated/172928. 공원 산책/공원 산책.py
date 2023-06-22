def solution(park, routes):
    answer = []
    posx = 0
    posy = 0
    boundx = len(park)
    boundy = len(park[0])
    boundchk = 0
    block = []
    
    for x in range(len(park)):
        for y in range(len(park[x])):
            if park[x][y] == 'S':
                posx = x
                posy = y
            
    for i in range(len(routes)):
        if routes[i][0] == 'N':
            if posx - int(routes[i][2]) < 0:
                continue
            else:
                for j in range(1, int(routes[i][2])+1):
                    if park[posx-j][posy] == 'X':
                        boundchk = 1
                        break
                
                if boundchk == 1:
                    boundchk = 0
                    continue
                
                posx -= int(routes[i][2])
        elif routes[i][0] == 'E':
            if posy + int(routes[i][2]) >= boundy:
                continue
            else:
                for j in range(1, int(routes[i][2])+1):
                    if park[posx][posy+j] == 'X':
                        boundchk = 1
                        break
                
                if boundchk == 1:
                    boundchk = 0
                    continue
                
                posy += int(routes[i][2])
        elif routes[i][0] == 'S':
            if posx + int(routes[i][2]) >= boundx:
                continue
            else:
                for j in range(1, int(routes[i][2])+1):
                    if park[posx+j][posy] == 'X':
                        boundchk = 1
                        break
                
                if boundchk == 1:
                    boundchk = 0
                    continue
                
                posx += int(routes[i][2])
        elif routes[i][0] == 'W':
            if posy - int(routes[i][2]) < 0:
                continue
            else:
                for j in range(1, int(routes[i][2])+1):
                    if park[posx][posy-j] == 'X':
                        boundchk = 1
                        break
                
                if boundchk == 1:
                    boundchk = 0
                    continue
                
                posy -= int(routes[i][2])
        
    answer.append(posx)
    answer.append(posy)
    
    return answer