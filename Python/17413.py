import sys
input = sys.stdin.readline

r_stack = []
o_stack = []
check = 0 # 1은 original 0은 reverse

S = list(input())

for word in S:
  if word == '<':
    if len(r_stack) != 0:
      r_stack.reverse()
      print(''.join(r_stack), end='')
      r_stack.clear()

    o_stack.append(word)
    check = 1
  elif word == '>':
    o_stack.append(word)
    print(''.join(o_stack), end='')
    o_stack.clear()
    check = 0
  elif word == ' ' or word == '\n':
    if check == 0:
      r_stack.reverse()
      print(''.join(r_stack), end=' ')
      r_stack.clear()
    else:
      o_stack.append(word)
  else:
    if check == 0:
      r_stack.append(word)
    else:
      o_stack.append(word)
  