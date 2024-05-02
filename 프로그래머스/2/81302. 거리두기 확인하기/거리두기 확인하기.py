def checkdist(place, i, j):
    if i-1 > -1:
        if place[i-1][j] == 'P':
            return True
        elif place[i-1][j] == 'O':
            if j-1 > -1:
                if place[i-1][j-1] == 'P':
                    return True
            if i-2 > -1:
                if place[i-2][j] == 'P':
                    return True
            if j+1 < 5:
                if place[i-1][j+1] == 'P':
                    return True
    if j-1 > -1:
        if place[i][j-1] == 'P':
            return True
        elif place[i][j-1] == 'O':
            if i-1 > -1:
                if place[i-1][j-1] == 'P':
                    return True
            if j-2 > -1:
                if place[i][j-2] == 'P':
                    return True
            if i+1 < 5:
                if place[i+1][j-1] == 'P':
                    return True
    if i+1 < 5:
        if place[i+1][j] == 'P':
            return True
        elif place[i+1][j] == 'O':
            if j-1 > -1:
                if place[i+1][j-1] == 'P':
                    return True
            if i+2 < 5:
                if place[i+2][j] == 'P':
                    return True
            if j+1 < 5:
                if place[i+1][j+1] == 'P':
                    return True
    if j+1 < 5:
        if place[i][j+1] == 'P':
            return True
        elif place[i][j+1] == 'O':
            if i-1 > -1:
                if place[i-1][j+1] == 'P':
                    return True
            if j+2 < 5:
                if place[i][j+2] == 'P':
                    return True
            if i+1 < 5:
                if place[i+1][j+1] == 'P':
                    return True
    return False
def solution(places):
    answer = []
    chk = 0
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if checkdist(place, i, j):
                        chk = 1
                        break
            if chk == 1:
                break
        if chk == 1:
            answer.append(0)
            chk = 0
        else:
            answer.append(1)
        
    return answer