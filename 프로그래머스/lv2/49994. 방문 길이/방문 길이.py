def solution(dirs):
    answer = 0
    pos = [0, 0]
    pos1 = pos.copy()
    way = []
    road = 0
    
    for d in dirs:
        if d == 'U':
            pos1[1] += 1
            if pos1[1] > 5:
                pos1[1] = 5
                continue
        elif d == 'D':
            pos1[1] -= 1
            if pos1[1] < -5:
                pos1[1] = -5
                continue
        elif d == 'R':
            pos1[0] += 1
            if pos1[0] > 5:
                pos1[0] = 5
                continue
        elif d == 'L':
            pos1[0] -= 1
            if pos1[0] < -5:
                pos1[0] = -5
                continue
        
        if len(way) == 0:
            way.append([pos, pos1])
            answer += 1
            pos = pos1.copy()
            pos1 = pos.copy()
        else:
            for w in way:
                if pos == w[0] and pos1 == w[1]:
                    pos = pos1.copy()
                    pos1 = pos.copy()
                    road = 1
                    break
                
                if pos == w[1] and pos1 == w[0]:
                    pos = pos1.copy()
                    pos1 = pos.copy()
                    road = 1
                    break
            if road == 0:
                answer += 1
                way.append([pos, pos1])
                pos = pos1.copy()
                pos1 = pos.copy()
            else:
                road = 0
    return answer