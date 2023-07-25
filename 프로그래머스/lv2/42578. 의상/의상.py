from collections import defaultdict

def solution(clothes):
    answer = 1
    cloth = defaultdict(list)
    
    for i in range(len(clothes)):
        cloth[clothes[i][1]].append(clothes[i][0])
    
    for j in cloth:
        answer *= (len(cloth[j]) + 1)
    
    return answer-1