for test_case in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))
    orderN = int(input())
    order_list = list(input().split())
    i = 0
    while i < len(order_list):
        if order_list[i] == 'I':
            start = int(order_list[i+1])
            count = int(order_list[i+2])
            orders = order_list[i+3:i+3+count]
            original[start:start] = orders
            i += 3 + count
        elif order_list[i] == 'D':
            start = int(order_list[i+1])
            count = int(order_list[i+2])
            del original[start:start+count]
            i += 3
        elif order_list[i] == 'A':
            count = int(order_list[i+1])
            for j  in range(count):
                original.append(order_list[i+2+j])
            i += 2 + count
    print(f"#{test_case} ", *original[:10])