import sys
input = sys.stdin.readline

num = input().rstrip()

num = int(num, 2)
num = oct(num)

print(num[2:])