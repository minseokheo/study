code_dict = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]
    for i in range(N):
        if '1' in code[i]:
            real_code = ""
            for j in range(len(code[i])-1, -1, -1):
                if code[i][j] == '1':
                    for k in range(j, j-56, -1):
                        real_code = code[i][k] + real_code
                    break
            break
            
    num_list = list()
    for i in range(8):
        num_list.append(code_dict[real_code[i*7:i*7+7]])
    odd_sum = 0
    even_sum = 0
    for i in range(8):
        if i % 2 == 0:
            odd_sum += num_list[i]
        else:
            even_sum += num_list[i]
    
    if (odd_sum*3 + even_sum) % 10 == 0:
        print(f"#{test_case}", sum(num_list))
    else:
        print(f"#{test_case} 0")