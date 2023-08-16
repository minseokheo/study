# 최초에 생각했을 때는 n의 갯수가 적은 만큼
# 어느 전력망을 잘라야 최솟값이 되는지 알 수 없다고 생각하여 한개씩 모두 잘라보고 비교하는 프로그램을 작성할 것입니다.
from collections import defaultdict, deque
def solution(n, wires):
    answer = -1
    diff = []
    for i in range(len(wires)):
        # 한개씩 자름
        w = wires.copy()
        w.pop(i)
        
        # 잘린 wires를 제외하고 나머지를 dictionary를 이용해서 나타냄
        wire_dict = defaultdict(list)
        for x, y in w:
            wire_dict[x].append(y)
            wire_dict[y].append(x)
        
        # 한개의 트리의 갯수만 알아내면 차이를 구할 수 있음
        # 따라서 한 개의 트리의 갯수를 알아냄
        tree = 0
        check = [0 for _ in range(n+1)]
        q = deque()
        q.append(1)
        while q:
            a = q.popleft()
            if check[a] == 0:
                tree += 1
                check[a] = 1
            else:
                continue
            for i in wire_dict[a]:
                q.append(i)
        diff.append(abs(tree-(n-tree)))
        
    answer = min(diff)
    return answer