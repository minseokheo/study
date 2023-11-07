for test_case in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))
    orderN = int(input())
    orders = list(input().split())
    i = 0
    while i < len(orders):
        if orders[i] == 'I':
            start = int(orders[i+1])
            count = int(orders[i+2])
            order_list = list(map(int, orders[i+3:i+3+count]))
            for order in order_list:
                original.insert(start, order)
                start += 1
            i += 3 + count
        elif orders[i] == 'D':
            start = int(orders[i+1])
            count = int(orders[i+2])
            for _ in range(count):
                original.pop(start)
            i += 3
    print(f"#{test_case}", end = ' ')
    for j in range(10):
        print(original[j], end= ' ')
    print()