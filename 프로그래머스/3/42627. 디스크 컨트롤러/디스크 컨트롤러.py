def solution(jobs):
    time, answer, length = 0, 0, len(jobs)
    jobs.sort(key = lambda x:x[1])
    while len(jobs) > 0:
        for i in jobs:
            if i[0] <= time:
                jobs.remove(i)
                time += i[1] - 1
                answer += time - i[0] +1
                break
        time += 1
    return answer//length 