n = int(input())
num_list = list()
stack = list()
print_list = list()

def pop():
  stack.pop()
  print_list.append('-')

def push(appendable):
  stack.append(appendable+1)
  print_list.append('+')
  return appendable + 1

def snum_list(n, nlist):
  appendable = 0
  for num in nlist:
    if appendable < num:
      for i in range(appendable, num):
        appendable = push(appendable)
    if stack[-1] == num:
      pop()


for i in range(n):
  num_list.append(int(input()))

snum_list(n, num_list)

if len(stack) == 0:
  for i in print_list:
    print(i)
else:
  print("NO")