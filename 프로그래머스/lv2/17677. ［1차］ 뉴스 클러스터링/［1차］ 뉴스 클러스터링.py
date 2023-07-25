def strtoset(s):
    s = s.lower()
    st = ''
    sset = []
    for i in range(len(s)):
        if i == 0 and s[i].isalpha():
            st += s[i]
        else:
            if s[i].isalpha():
                st += s[i]
            else:
                st = ''
            if len(st) == 2:
                sset.append(st)
                st = s[i]
    return sset

def solution(str1, str2):
    answer = 0
    str1set = strtoset(str1)
    str2set = strtoset(str2)
    interset = 0
    sumset = 0
    
    if len(str1set) > len(str2set):
        for i in range(len(str1set)):
            if str1set[i] in str2set:
                str2set.remove(str1set[i])
                interset += 1
        sumset = len(str1set) + len(str2set)

        if sumset == 0:
            answer = 65536
        else:
            answer = int(interset / sumset * 65536)
    else:
        for i in range(len(str2set)):
            if str2set[i] in str1set:
                str1set.remove(str2set[i])
                interset += 1
        sumset = len(str1set) + len(str2set)

        if sumset == 0:
            answer = 65536
        else:
            answer = int(interset / sumset * 65536)
    return answer