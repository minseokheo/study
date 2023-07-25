def solution(msg):
    answer = []
    alphadict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    index = 27
    stack = ""
    i = 0
    
    while i < len(msg):
        for j in range(i, len(msg)):
            stack += msg[j]
            if stack not in alphadict:
                alphadict[stack] = index
                index += 1
                answer.append(alphadict[stack[:-1]])
                i = j
                break
            else:
                if j == len(msg)-1 and i == len(msg)-1:
                    answer.append(alphadict[stack])
                    i += 1
                elif j == len(msg)-1:
                    answer.append(alphadict[stack])
                    i = len(msg)
        stack = ""
            
        
    return answer