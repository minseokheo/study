import sys
input = sys.stdin.readline

N = int(input())
exp = list(input().rstrip())
num_list = [0] * N
stack = []
num1, num2 = 0, 0

for i in range(N):
  num_list[i] = int(input())

for part in exp:
  if 'A' <= part <= 'Z':
    stack.append(num_list[ord(part)-ord('A')])
  else:
    num2 = stack.pop()
    num1 = stack.pop()

    if part == '+':
      stack.append(num1 + num2)
    elif part == '-':
      stack.append(num1 - num2)
    elif part == '*':
      stack.append(num1 * num2)
    elif part == '/':
      stack.append(num1 / num2)

print("{:.2f}".format(stack.pop()))