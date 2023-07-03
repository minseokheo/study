def solution(elements):
    answer = 0
    l = len(elements)
    elements = elements + elements[:-1]
    sumel = []
    
    for i in range(l):
        j = 1
        while j <= l:
            num = sum(elements[i:i+j])
            sumel.append(num)
            j += 1
        
    answer = len(list(set(sumel)))
    
    return answer