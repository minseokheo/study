import sys
input = sys.stdin.readline

white = 0
blue = 0

def one_divide(paper, n):
    new_paper = list()
    for i in range(n//2):
        new_paper.append(paper[i][:n//2])
    
    return new_paper

def two_divide(paper, n):
    new_paper = list()
    for i in range(n//2):
        new_paper.append(paper[i][n//2:])

    return new_paper

def three_divide(paper, n):
    new_paper = list()
    for i in range(n//2):
        new_paper.append(paper[n//2+i][:n//2])
    
    return new_paper

def four_divide(paper, n):
    new_paper = list()
    for i in range(n//2):
        new_paper.append(paper[n//2+i][n//2:])

    return new_paper

def divide_and_conquer(paper, n):
    global white
    global blue
    if n == 1:
        if paper[0][0] == 1:
            blue += 1
            return
        else:
            white += 1
            return
    color = -1
    chk = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                color = paper[i][j]
            elif color != paper[i][j]:
                chk = 1
                break
        if chk == 1:
            break
    if chk == 1:
        divide_and_conquer(one_divide(paper, n), n//2)
        divide_and_conquer(two_divide(paper, n), n//2)
        divide_and_conquer(three_divide(paper, n), n//2)
        divide_and_conquer(four_divide(paper, n), n//2)
    else:
        if color == 1:
            blue += 1
        else:
            white += 1

N = int(input())
paper = list()

for _ in range(N):
    paper.append(list(map(int, input().split())))

divide_and_conquer(paper, N)

print(white)
print(blue)