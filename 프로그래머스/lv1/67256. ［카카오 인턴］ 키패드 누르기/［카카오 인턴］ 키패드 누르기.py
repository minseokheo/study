def solution(numbers, hand):
    answer = ''
    lefthand = [3, 0]
    righthand = [3, 2]
    diffleft = -1
    diffright = -1
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    
    for n in numbers:
        if n == 1:
            answer += 'L'
            lefthand = [0, 0]
        elif n == 4:
            answer += 'L'
            lefthand = [1, 0]
        elif n == 7:
            answer += 'L'
            lefthand = [2, 0]
        elif n == 3:
            answer += 'R'
            righthand = [0, 2]
        elif n == 6:
            answer += 'R'
            righthand = [1, 2]
        elif n == 9:
            answer += 'R'
            righthand = [2, 2]
        else:
            for i in range(len(keypad)):
                for j in range(len(keypad[i])):
                    if keypad[i][j] == n:
                        choosehand = [i, j]
            diffleft = abs(lefthand[0]-choosehand[0]) + abs(lefthand[1]-choosehand[1])
            diffright = abs(righthand[0]-choosehand[0]) + abs(righthand[1]-choosehand[1])
                
            if diffleft > diffright:
                righthand = choosehand
                answer += 'R'
            elif diffleft < diffright:
                lefthand = choosehand
                answer += 'L'
            else:
                if hand == 'right':
                    righthand = choosehand
                    answer += 'R'
                elif hand == 'left':
                    lefthand = choosehand
                    answer += 'L'
    return answer