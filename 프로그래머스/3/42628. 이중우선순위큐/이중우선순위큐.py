def solution(operations):
    answer = []
    queue = []
    for op in operations:
        if op[0] == 'I':
            queue.append(int(op[2:]))
        else:
            if op[2:] == '1':
                if queue:
                    queue.remove(max(queue))
            else:
                if queue:
                    queue.remove(min(queue))
    
    if not queue:
        answer = [0, 0]
    else:
        answer = [max(queue), min(queue)]
                    
    return answer