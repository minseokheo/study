def solution(brown, yellow):
    answer = []
    s = brown + yellow
    height = 0
    
    for width in range(s+1, 1, -1):
        if s % width == 0:
            height = s // width
            if (width-2) * (height-2) == yellow:
                return [width, height]