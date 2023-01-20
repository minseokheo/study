import sys
input = sys.stdin.readline

exp = list(input().rstrip())
stack = []
res = ''

for part in exp:
  if part.isalpha():
    res += part
  else:
    if part == '(':
      stack.append(part)
    elif part == '*' or part == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        res += stack.pop()
      stack.append(part)
    elif part == '+' or part == '-':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.append(part)
    elif part == ')':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.pop()

while stack:
  res += stack.pop()

print(res)