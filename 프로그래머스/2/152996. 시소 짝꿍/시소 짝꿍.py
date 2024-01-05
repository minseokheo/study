from collections import defaultdict
def solution(weights):
    answer = 0
    # 시간초과
#     weights.sort()
#     l = len(weights)
    
#     for i in range(l-1):
#         for j in range(i+1, l):
#             if weights[i] == weights[j]:
#                 answer += 1
#             elif (weights[i] * 3) == (weights[j] * 2):
#                 answer += 1
#             elif (weights[i] * 2) == weights[j]:
#                 answer += 1
#             elif (weights[i] * 4) == (weights[j] * 3):
#                 answer += 1

    weights.sort()
    wd = defaultdict(int)
    
    for weight in weights:
        if wd[weight]:
            answer += wd[weight]
        wd[weight] += 1
        
        if weight % 2 == 0:
            wd[weight//2*3] += 1
        
        if weight % 3 == 0:
            wd[weight//3*4] += 1
        
        wd[weight*2] += 1
    
    return answer