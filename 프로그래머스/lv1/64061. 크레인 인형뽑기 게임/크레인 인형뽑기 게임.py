def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                item = board[i][move-1]
                board[i][move-1] = 0
                basket.append(item)
                break
        
        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer