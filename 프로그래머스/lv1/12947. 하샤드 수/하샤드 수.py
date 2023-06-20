def solution(x):
    answer = True
    num = sum(list(map(int, str(x))))
    if x % num == 0:
        answer = True
    else:
        answer = False
    return answer