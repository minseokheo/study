import sys
input = sys.stdin.readline

N = int(input())
order = []
deque = []
front, rear = 0, 0

for i in range(N):
  order = list(input().split())

  if order[0] == 'push_back':
    deque.insert(rear, order[1])
    rear += 1
  elif order[0] == 'push_front':
    deque.insert(front, order[1])
    rear += 1
  elif order[0] == 'front':
    if front == rear:
      print("-1")
    else:
      print(deque[front])
  elif order[0] == 'back':
    if front == rear:
      print("-1")
    else:
      print(deque[rear-1])
  elif order[0] == 'size':
    print(rear - front)
  elif order[0] == 'empty':
    if front == rear:
      print("1")
    else:
      print("0")
  elif order[0] == 'pop_front':
    if front == rear:
      print("-1")
    else:
      print(deque[front])
      front += 1
  elif order[0] == 'pop_back':
    if front == rear:
      print("-1")
    else:
      print(deque[rear-1])
      rear -= 1