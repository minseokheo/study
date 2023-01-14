import sys
input = sys.stdin.readline

N = int(input())

order = []
stack = []
top = 0

for i in range(N):
  order = list(input().split())

  if order[0] == 'push':
    stack.append(int(order[1]))
    top += 1
  elif order[0] == 'top':
    if top == 0:
      print('-1')
    else:
      print(stack[top-1])
  elif order[0] == 'size':
    print(top)
  elif order[0] == 'empty':
    if top == 0:
      print('1')
    else:
      print('0')
  elif order[0] == 'pop':
    if top == 0:
      print('-1')
    else:
      print(stack[top-1])
      del(stack[top-1])
      top -= 1