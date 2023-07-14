def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for ind, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(ind)
    return answer