N = int(input())

vote_1 = 0
vote_0 = 0

for i in range(N):
  vote = int(input())

  if vote == 1:
    vote_1 += 1
  elif vote == 0:
    vote_0 += 1

if vote_1 < vote_0:
  print("Junhee is not cute!")
else:
  print("Junhee is cute!")