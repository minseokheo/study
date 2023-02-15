import sys
input = sys.stdin.readline

pipeline = list(input())
now_pipe = 0
total_pipe = 0
stack = []
top = 0

for char in pipeline:
  if char == '(':
    stack.append(char)
    top += 1
    now_pipe += 1
  elif char == ')':
    if stack[top-1] == '(': # razer
      now_pipe -= 1
      total_pipe += now_pipe
    elif stack[top-1] == ')':
      total_pipe += 1
      now_pipe -= 1
    stack.append(char)
    top += 1

print(total_pipe)