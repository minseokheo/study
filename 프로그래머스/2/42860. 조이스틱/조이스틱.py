def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2):
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        print(left_moved)
        print(right_moved)
        print([left_moved, right_moved[0]+right_moved[:0:-1]])
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer