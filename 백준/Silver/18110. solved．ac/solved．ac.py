import sys
input = sys.stdin.readline

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())

if n == 0:
    print(0)
    exit()

opinion = list()

for _ in range(n):
    op = int(input())
    opinion.append(op)

opinion.sort()

cut = my_round(n * 0.15)


if cut == 0:
    print(my_round(sum(opinion)/len(opinion)))
else:
    print(my_round(sum(opinion[cut:-cut])/len(opinion[cut:-cut])))