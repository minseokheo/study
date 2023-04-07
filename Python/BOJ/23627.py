input_word = input()

S = list(input_word)

cute_word = list("driip")

if S[-5:] == cute_word:
  print("cute")
else:
  print("not cute")