def solution(book_time):
    answer = 1
    n = len(book_time)
    book_time.sort(key=lambda x:x[0])
    chk = [False] * n
    
    for i in range(n):
        book_time[i][0] = int(book_time[i][0][:2])*60 + int(book_time[i][0][3:])
        book_time[i][1] = int(book_time[i][1][:2])*60 + int(book_time[i][1][3:]) + 10
    
    rooms = [0]
    
    for i in range(n):
        possible = False
        for j in range(len(rooms)):
            if rooms[j] <= book_time[i][0]:
                rooms[j] = book_time[i][1]
                possible = True
            if possible == True:
                break
        if possible == False:
            rooms.append(book_time[i][1])
            answer += 1
    return answer