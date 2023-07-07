import string
tmp = string.digits+string.ascii_uppercase

def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    numlist = []
    for i in range(t*m):
        s = convert(i, n)
        for j in range(len(s)):
            numlist.append(s[j])
    for i in range(p-1, t*m, m):
        answer += numlist[i]
    return answer