# 최초 선택한 고안은 처음부터 한개씩 추가하면서 k값이랑 비교해서 k값보다 커지면 앞의 인덱스를 추가해서 비교하는 방법
def solution(sequence, k):
    """
    answer = [0, len(sequence)-1]
    index = [0, 0]
    
    for i in range(len(sequence)):
        index[1] = i
        if sum(sequence[index[0]:index[1]+1]) < k:
            continue
        elif sum(sequence[index[0]:index[1]+1]) == k:
            if index[1] - index[0] == 0:
                answer = index
                break
            if (answer[1] - answer[0]) > (index[1] - index[0]):
                answer[0] = index[0]
                answer[1] = index[1]
        else:
            while sum(sequence[index[0]:index[1]+1]) > k:
                index[0] += 1
                if sum(sequence[index[0]:index[1]+1]) == k:
                    if index[1] - index[0] == 0:
                        answer = index
                        return answer
                    if (answer[1] - answer[0]) > (index[1] - index[0]):
                        answer[0] = index[0]
                        answer[1] = index[1]
    """
    # 하지만 이 방법은 시간초과가 9 ~ 16 테스트케이스, 24 ~ 30 테스트케이스에서 걸리게 됨
    # 새로 생각해낸 방법은 아예 인덱스를 따로 두고 오름차순을 이용해서 해 보려고 함
    answer = []
    l = len(sequence)
    part_sum = sequence[0]
    right = 0
    
    for left in range(l):
        while right+1 < l and part_sum < k:
            right += 1
            part_sum += sequence[right]
        
        if part_sum == k:
            if not answer:
                answer.append(left)
                answer.append(right)
            else:
                if (answer[1] - answer[0]) > right - left:
                    answer[0], answer[1] = left, right
        
        part_sum -= sequence[left]
    
        
    return answer