import sys
input = sys.stdin.readline

T = int(input())
sentence = []
stack = []

for i in range(T):
  sentence = list(input())
  
  for word in sentence:
    if word != " " and word != "\n":
      stack.append(word)
    else:
      stack.reverse()
      for w in stack:
        print(w, end='')
      print(end=' ')
      stack.clear()
  print()      