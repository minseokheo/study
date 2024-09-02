def solution(array, commands):
    answer = []
    for com in commands:
        i, j, k = com[0], com[1], com[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer