def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    i = 0
    while i < len(alpha):
        if alpha[i] in skip:
            alpha = alpha[:i] + alpha[i+1:]
        else:
            i += 1
    
    for a in range(len(s)):
        b = alpha.index(s[a]) + index
        if b >= len(alpha):
            b %= len(alpha)
        answer += alpha[b]
    return answer