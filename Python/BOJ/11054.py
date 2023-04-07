import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1]
dp_inc = [0 for _ in range(N)]
dp_dec = [0 for _ in range(N)]
dp_sum = [0 for _ in range(N)]
dp_inc[0] = 1
dp_dec[0] = 1

for i in range(1, N):
  for j in range(i):
    if A[j] < A[i]:
      dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
    else:
      dp_inc[i] = max(dp_inc[i], 1)

for i in range(1, N):
  for j in range(i):
    if reverse_A[j] < reverse_A[i]:
      dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)
    else:
      dp_dec[i] = max(dp_dec[i], 1)

dp_dec.reverse()
dp_sum = [x + y for x, y in zip(dp_inc, dp_dec)]

print(max(dp_sum)-1)