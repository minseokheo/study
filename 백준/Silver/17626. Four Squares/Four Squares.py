import sys
input = sys.stdin.readline

# 1 - 1개, 2 - 2개, 3 - 3개, 4 - 1개, 5 - 2개, 6 - 3개
# 7 - 4개, 8 - 2개, 9 - 1개, 10 - 2개, 11 - 3개, 12 - 3개
# 13 - 2개, 14 - 3개, 15 - 4개, 16 - 1개, 17 - 2개, 18 - 2개
# 19 - 3개, 20 - 2개, 21 - 3개, 22 - 3개, 

n = int(input())
d = [0 for _ in range(n+1)]
d[1] = 1

for i in range(2, n+1):

    j = 1
    min_val = 5
    while j**2 <= i:
        min_val = min(min_val, d[i-j**2])
        j += 1
    
    d[i] = min_val + 1

print(d[n])