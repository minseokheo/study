import numpy as np
global arrcount0, arrcount1
arrcount0 = 0
arrcount1 = 0

def dandc(arr, w, h):
    global arrcount0, arrcount1
    if w == 1 and h == 1:
        if arr[0][0] == 1:
            arrcount1 += 1
            return
        else:
            arrcount0 += 1
            return
        
    count0 = 0
    count1 = 0
    
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                count1 += 1
            else:
                count0 += 1
                
    if count1 == w*h:
        arrcount1 += 1
        return
    elif count0 == w*h:
        arrcount0 += 1
        return
    else:
        dandc(arr[0:h//2, 0:w//2], w//2, h//2)
        dandc(arr[h//2:h, 0:w//2], w//2, h//2)
        dandc(arr[0:h//2, w//2:w], w//2, h//2)
        dandc(arr[h//2:h, w//2:w], w//2, h//2)
        
def solution(arr):
    global arrcount0, arrcount1
    answer = []
    w = len(arr[0])
    h = len(arr)
    arr = np.array(arr)
    dandc(arr, w, h)
    answer.append(arrcount0)
    answer.append(arrcount1)
    return answer