def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
            if j == len(prices)-1:
                answer.append(j-i)
    answer.append(0)
    return answer

# print(solution([1, 3, 3, 2, 4, 3, 1]))