def solution(numbers):
    answer = []
    while numbers:
        num = numbers.pop(0)
        num_2 = bin(num)
        count1 = 0
        if num_2[-1] == '0':
            answer.append(num+1)
        else:
            for i in range(len(num_2)-1, -1, -1):
                if num_2[i] == '1':
                    count1 += 1
                else:
                    answer.append(num + (2 ** (count1-1)))
                    break
    return answer