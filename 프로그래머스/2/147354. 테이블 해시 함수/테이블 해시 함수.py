def solution(data, col, row_begin, row_end):
    answer = 0
    s_data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        l = len(s_data[i-1])
        r = 0
        for j in range(l):
            r += s_data[i-1][j] % i
        if answer == 0:
            answer = r
        else:
            answer = answer^r
    return answer