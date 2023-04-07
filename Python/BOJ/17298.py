import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
answer = [-1] * N

for i in range(N):
  while stack and arr[stack[-1]] < arr[i]:
    answer[stack.pop()] = arr[i]
  
  stack.append(i)

print(*answer)