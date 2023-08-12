# 처음 생각해낸 방법은 직관적으로 하나하나 다 찾아서 갯수를 센 다음 정답을 구하는 방식입니다.
# 이 방법은 시간복잡도가 굉장히 복잡할 것으로 생각했지만 제한사항에 조건의 경계가 작다는 점을 생각해서
# 시간복잡도가 조금 더 걸려도 괜찮다고 생각했습니다.

from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        order_dict = {} # 주문을 받은 갯수를 저장하는 dictionary입니다.
        for order in orders:
            order = ''.join(sorted(order)) # 주문의 순서가 뒤죽박죽 들어오는 것을 대비해 미리 정렬을 시켜놓습니다.
            for x in combinations(order, c): # combinations 함수를 이용해서 모든 조합을 뽑아냅니다.
                if x not in order_dict:
                    order_dict[x] = 1
                else:
                    order_dict[x] += 1
                    
        order_dict = sorted(order_dict.items(), key=lambda x:x[1], reverse=True)
        
        if order_dict:
            maxval = order_dict[0][1]
            if maxval < 2: # 해당 조합이 2번이상 나와야 코스요리로 인정되므로 2번보다 작게 나왔다면 넘어갑니다.
                continue
        else:
            continue
        
        for i in range(len(order_dict)):
            if order_dict[i][1] == maxval:
                answer.append(''.join(order_dict[i][0]))
            else:
                break
    
    answer.sort()
    return answer