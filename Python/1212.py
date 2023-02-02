import sys
input = sys.stdin.readline

num = input()
print(bin(int(num, 8))[2:])