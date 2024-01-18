import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def cal(a, b):
    return (a+b)*(a-b)

print(cal(A, B))