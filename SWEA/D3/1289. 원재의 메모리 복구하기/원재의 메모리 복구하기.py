T = int(input())
for test_case in range(1, T + 1):
    st = list(map(int, input()))
    for i in range(len(st)):
        if  i == 0:
            if st[i] == 0:
                ans = 0
                last_chk = 0
            else:
                ans = 1
                last_chk = 1
        else:
            if st[i] == 0 and last_chk == 1:
                ans += 1
                last_chk = 0
            elif st[i] == 1 and last_chk == 0:
                ans += 1
                last_chk = 1
    print(f"#{test_case} {ans}")