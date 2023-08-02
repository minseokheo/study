def solution(n):
    
    length = 0
    for i in range(n, 0, -1): # 전체 길이를 알 수 있도록 for문을 돌려준다
        length += i
    answer = [0 for _ in range(length)] # 전체 길이로 미리 0으로 초기화 시켜둔다
    direction = {'down': 'right', # 방향을 바꿔 줄 dictionary
                 'right': 'up', 
                 'up': 'down'}
    d = 'down' # 초기 방향은 down
    idx = 0 # index 위치
    val = 1 # 해당하는 index에 들어갈 값
    index_interval = 1 # index가 순서대로 올라가는게 아니기 때문에 규칙을 찾았음
    while val <= length:
        a = 1 # a는 한 iteration당 들어갈 숫자의 갯수
        while a < n+1:
            if a == n:
                d = direction[d] # 방향을 바꿔줌
            
            answer[idx] = val
            val += 1
            
            # 아래, 위로, 오른쪽으로 갈때 indexing이 다르기 때문에 구분지어 줌
            if d == 'down': # 아래로 내려갈 경우
                idx = idx + index_interval
                index_interval += 1
            elif d == 'right': # 오른쪽으로 이동하는 경우
                idx = idx + 1
            elif d == 'up': # 위로 올라가는 경우
                idx = idx - index_interval
                index_interval -= 1
            a += 1
        n -= 1
    
    # 위의 코드로 생각하니 하나하나 하드코딩하게 되는 꼴이라 딕셔너리 방법으로 생각하기로 했음
    """
    numdict = {}
    key = 1
    val = 1
    
    length = 0
    for i in range(n, 0, -1): # 전체 길이를 알 수 있도록 for문을 돌려준다
        length += i
    
    for i in range(1, length+1): # 번호를 한개 한개 idx 위치에 따라 넣을 것이다
        a = 0 # a는 한 반복문당 넣을 숫자의 갯수
        while a != n:
            
            a += 1
        n -= 1
    """
    # 다시 생각하니까 더 구현이 어려울듯...함.. 다시 위의 방식대로 index를 노트에 하나하나 써가면서 규칙을 찾아봄
    return answer