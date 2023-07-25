def solution(s):
    answer = ''
    s = s.lower()
    i = 0
    word = ''
    while i < len(s):
        if i == 0:
            if s[i].isalpha():
                word = s[i].upper()
                answer += word
                i += 1
        else:
            if s[i-1] == ' ':
                if s[i].isalpha():
                    word = s[i].upper()
                    answer += word
                    i += 1
        
        if i < len(s):
            answer += s[i]
        i += 1
    return answer