def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]        
    report2 = [[0 for j in range(len(id_list))] for i in range(len(id_list))]
    
    for call in report:
        a, b = call.split()
        report2[id_list.index(b)][id_list.index(a)] = 1
    
    for i in range(len(report2)):
        if sum(report2[i]) >= k:
            for j in range(len(report2[i])):
                answer[j] += report2[i][j]
    return answer