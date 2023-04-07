V = int(input())

vote = list(input())
a_vote = 0
b_vote = 0

for i in range(V):
  if vote[i] == 'A':
    a_vote += 1
  else:
    b_vote += 1


if a_vote > b_vote:
  print("A")
elif a_vote < b_vote:
  print("B")
else:
  print("Tie")
