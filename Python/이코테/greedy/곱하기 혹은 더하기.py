import sys
input = sys.stdin.readline

data = input().rstrip()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    
    if int(num) <= 1 or result <= 1:
        result += int(num)
    else:
        result *= int(num)

print(result)