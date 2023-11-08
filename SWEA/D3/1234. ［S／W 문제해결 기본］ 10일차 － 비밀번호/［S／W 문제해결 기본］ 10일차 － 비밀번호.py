for test_case in range(1, 11):
    order = list(input().split())
    N = int(order[0])
    original = list(order[1])
    index = 0
    while index < len(original)-1:
        if original[index] == original[index+1]:
            del original[index:index+2]
            index -= 1
        else:
            index += 1
    print(f"#{test_case} ", ''.join(original))