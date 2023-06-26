def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        press = 0
        for j in range(len(targets[i])):
            minindex = 999
            for a in range(len(keymap)):
                if keymap[a].find(targets[i][j]) != -1:
                    if minindex > keymap[a].find(targets[i][j]):
                        minindex = keymap[a].find(targets[i][j])
            if minindex == 999:
                press = -1
                break
            else:
                press += minindex+1
            
        answer.append(press)
    return answer