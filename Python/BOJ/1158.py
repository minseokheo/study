import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cur = K
queue = []
queue.append(-1)
del_list = []

for i in range(1, N+1):
  queue.append(i)

for j in range(1, N+1):
  del_list.append(queue[cur])
  queue.remove(queue[cur])
  cur += K-1

  if N != j:
    while cur > N-j:
      cur -= N-j

print("<", end='')

for k in range(len(del_list)):
  if k != len(del_list)-1:
    print(del_list[k], end=', ')
  else:
    print(del_list[k], end='')

print(">")