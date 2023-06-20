from itertools import permutations
def solution(babbling):
    answer = 0
    a = ['aya', 'ye', 'woo', 'ma']
    c = list(map(''.join, permutations(a,2)))
    d = list(map(''.join, permutations(a,3)))
    e = list(map(''.join, permutations(a,4)))
    for b in babbling:
        if b in a:
            answer += 1
        elif b in c:
            answer += 1
        elif b in d:
            answer += 1
        elif b in e:
            answer += 1
    return answer

b = list(input().split())
print(solution(b))