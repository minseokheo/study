import sys
input = sys.stdin.readline

T = int(input())
data = []
stack = []
top = 0
check = 1

for i in range(T):
  data = list(input())
  for ps in data:
    if ps == '(':
      stack.append(ps)
      top += 1
    elif ps == ')':
      if top == 0:
        check = 0
        break
      else:
        del(stack[top-1])
        top -= 1
  if check == 0 or len(stack) != 0:
    print("NO")
  else:
    print("YES")  
  check = 1
  stack.clear()
  top = 0