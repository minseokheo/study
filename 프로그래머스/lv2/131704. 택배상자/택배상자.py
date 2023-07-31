# 문제의 첫번째(벨트에 놓인 순서대로) 두번째 단락(입구 외에 다른 면이 막혀있어서 맨 앞의 상자만 뺄 수 있습니다.)을
# 읽었을때 stack을 이용해서 풀어야할것같다고 생각이 들었음

def solution(order):
    answer = 0
    """
    boxes = len(order)
    
    # 영재의 컨테이너 벨트
    belt = [i for i in range(boxes, 0, -1)]
    
    # 보조 컨테이너 벨트(스택 활용)
    subbelt = list()
    subtop = 0
    
    for box in order: # order에서 한 개씩 꺼내서 뺄 수 있는지 확인
        if box in belt: # box가 영재의 컨테이너 벨트에 있으면
            while True: 
                b = belt.pop()
                if box == b: # belt에서 꺼낸게 box랑 일치하면 트럭에 싣기
                    answer += 1
                    break
                else: # 일치하지 않으면 보조 컨테이너 벨트에 넣기
                    subbelt.append(b)
                    subtop += 1
        else: # box가 영재의 컨테이너 벨트에 없으면(이미 영재 벨트에서 보조 컨테이너 벨트로 갔다는 이야기)
            if box == subbelt[subtop-1]: # 보조 컨테이너 벨트에서 제일 최근에 넣은 것이 box랑 일치하면
                subbelt.pop()
                answer += 1
                subtop -= 1
            else:
                break    
    """
    
    # 위의 코드는 시간초과 발생.. (아마도 while 반복문에서 시간복잡도를 해결 못한듯..)
    
    boxes = len(order)
    idx = 1
    
    # 보조 컨테이너 벨트(스택 활용)
    subbelt = list()
    subtop = 0
    
    while idx < boxes+1: # 컨테이너 벨트에 있는 갯수 만큼 반복
        subbelt.append(idx) # 일단 subbelt에 넣기
        
        while subbelt and subbelt[-1] == order[answer]: # subbelt의 제일 마지막 원소가 order가 같으면 => 트럭에 싣는다
            subbelt.pop()
            answer += 1
        
        idx += 1
        
    return answer