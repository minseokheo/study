S = list(input())
num_dict = {
  'ZERO': 0,
  'ONE': 1,
  'TWO': 2,
  'THREE': 3,
  'FOUR': 4,
  'FIVE': 5,
  'SIX': 6,
  'SEVEN': 7,
  'EIGHT': 8,
  'NINE': 9,
}
make_word = list()
expression = list()
operand = list()
operator = list()

for word in S:
  if word == '+':
    expression.append(word)
  elif word == '-':
    expression.append(word)
  elif word == 'x':
    expression.append(word)
  elif word == '/':
    expression.append(word)
  elif word == '=':
    expression.append(word)
  else:
    make_word.append(word)
    str_word = ''.join(map(str, make_word))
    if str_word in num_dict:
      expression.append(num_dict[str_word])
      make_word.clear()

print(''.join(map(str, expression)))

# postfix_stack = list()
# postfix_str = ""

# for ch in expression:
#   if ch == '+' or ch == '-':
#     postfix_stack.append(ch)
#   elif ch == 'x' or ch == '/':
#     postfix_stack.append(ch)
#   else:
#     postfix_str += ch

# while postfix_stack:
#   postfix_str += postfix_stack.pop()

# print(postfix_str)