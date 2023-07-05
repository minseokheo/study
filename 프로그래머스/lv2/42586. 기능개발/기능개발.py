def solution(progresses, speeds):
    answer = []
    speeds1 = speeds.copy()
    stack = []
    for i in range(len(progresses)):
        while True:
            waiting = progresses[i] + speeds1[i]
            if waiting >= 100:
                stack.append(1)
                break
            else:
                if stack:
                    answer.append(len(stack))
                    stack.clear()
                for j in range(i, len(speeds)):
                    speeds1[j] += speeds[j]
    if stack:
        answer.append(len(stack))
    return answer