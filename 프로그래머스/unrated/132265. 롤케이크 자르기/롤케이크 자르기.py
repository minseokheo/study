from collections import Counter
def solution(topping):
    answer = 0
    
    chul = set()
    bro = Counter(topping)
    
    for i in topping:
        bro[i] -= 1
        
        if bro[i] == 0:
            del bro[i]
        chul.add(i)
        
        if len(chul) == len(bro):
            answer += 1
    return answer