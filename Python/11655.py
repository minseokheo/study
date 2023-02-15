import sys
input = sys.stdin.readline

string = list(input().rstrip())
print_string = ""

for char in string:
  if char.isupper():
    if ord(char) + 13 >= 91:
      print_string += chr(ord(char)-13)
    else:
      print_string += chr(ord(char)+13)
  elif char.islower():
    if ord(char) + 13 >= 123:
      print_string += chr(ord(char)-13)
    else:
      print_string += chr(ord(char)+13)
  else:
    print_string += char
      
print(print_string)