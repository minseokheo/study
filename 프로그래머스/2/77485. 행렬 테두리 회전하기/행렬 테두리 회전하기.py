def solution(rows, columns, queries):
    answer = []
    # 배열 생성
    a = [[0 for _ in range(columns)] for _ in range(rows)]
    val = 1
    for i in range(rows):
        for j in range(columns):
            a[i][j] = val
            val += 1
            
    for query in queries:
        #움직이는 수 리스트
        movement = []
        #index 정리
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        #위
        for i in range(y1+1, y2+1):
            #밀자
            if i == y1+1:
                temp1 = a[x1][i-1]
            else:
                temp1 = temp2
            temp2 = a[x1][i]
            movement.append(temp1)
            a[x1][i] = temp1
        #오른쪽
        for i in range(x1+1, x2+1):
            #밀자
            temp1 = temp2
            temp2 = a[i][y2]
            movement.append(temp1)
            a[i][y2] = temp1
        #아래
        for i in range(y2-1, y1-1, -1):
            temp1 = temp2
            temp2 = a[x2][i]
            movement.append(temp1)
            a[x2][i] = temp1
        #왼쪽
        for i in range(x2-1, x1-1, -1):
            temp1 = temp2
            temp2 = a[i][y1]
            movement.append(temp1)
            a[i][y1] = temp1
        answer.append(min(movement))
        
    return answer