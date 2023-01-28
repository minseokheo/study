while True:
  try:
    print_list = [0 for i in range(4)]
    string = list(input())

    for char in string:
      if char.isupper():
        print_list[1] += 1
      elif char.islower():
        print_list[0] += 1
      elif char.isdigit():
        print_list[2] += 1
      elif char == " ":
        print_list[3] += 1

    print(*print_list)

  except EOFError:
    break