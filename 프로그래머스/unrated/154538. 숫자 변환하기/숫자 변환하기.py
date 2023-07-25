def solution(x, y, n):
    answer = -1
    arr = [[y, 0]]
    
    while arr:
        a = arr.pop(0)
        appendlist = []
        
        if a[0] == x:
            return a[1]
        
        if a[0] > x:
            if a[0] % 3 == 0:
                arr.append([a[0]//3, a[1]+1])
            if a[0] % 2 == 0:
                arr.append([a[0]//2, a[1]+1])
            arr.append([a[0]-n, a[1]+1])
            
    return answer