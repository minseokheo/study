import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    closet = dict()

    for _ in range(n):
        name, tp = map(str, input().split())

        if tp not in closet:
            closet[tp] = 1
        else:
            closet[tp] += 1

    # 1 - 1
    # 1 2 - 1+2 + 1*2 = 5
    # 1 2 3 - 1+2+3 + 1*2+1*3+2*3 + 1*2*3 = 23
    # 1 2 2 - 1+2+2 + 1*2+1*2+2*2 + 1*2*2 = 17
    # 앞에거 갯수 * (뒤에거 갯수+1) + 뒤에거 갯수
    
    count = 0
    for k, v in closet.items():
        count = count * (v+1) + v
    
    print(count)