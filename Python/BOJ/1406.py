import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
M = int(input())
order = []
stack2 = []

for i in range(M):
  order = list(input().split())
  
  if order[0] == 'P':
    stack1.append(order[1])
  elif order[0] == 'L':
    if stack1:
      stack2.append(stack1.pop())
  elif order[0] == 'D':
    if stack2:
      stack1.append(stack2.pop())
  elif order[0] == 'B':
    if stack1:
      stack1.pop()

stack1.extend(reversed(stack2))
print(''.join(stack1))