import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = [-1] * N
stack = [0]
counter = Counter(arr)

for i in range(1, N):
  while stack and counter[arr[stack[-1]]] < counter[arr[i]]:
    answer[stack.pop()] = arr[i]
  
  stack.append(i)

print(*answer)