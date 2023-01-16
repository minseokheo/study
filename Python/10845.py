import sys
input = sys.stdin.readline

N = int(input())
order = []
front, rear = 0, 0
queue = []

for i in range(N):
  order = list(input().split())

  if order[0] == 'push':
    queue.append(order[1])
    rear += 1
  elif order[0] == 'front':
    if front == rear:
      print("-1")
    else:
      print(queue[front])
  elif order[0] == 'back':
    if front == rear:
      print("-1")
    else:
      print(queue[rear-1])
  elif order[0] == 'size':
    print(rear-front)
  elif order[0] == 'empty':
    if front == rear:
      print("1")
    else:
      print("0")
  elif order[0] == 'pop':
    if front == rear:
      print("-1")
    else:
      print(queue[front])
      front += 1