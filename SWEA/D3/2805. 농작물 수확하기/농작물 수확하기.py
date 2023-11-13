T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    m = [[int(i) for i in input()] for _ in range(N)]
    ans = 0
    a, b = N//2, N//2+1
    for i in range(N):
        ans += sum(m[i][a:b])
        if i < N//2:
            a -= 1
            b += 1
        else:
            a += 1
            b -= 1
    print(f"#{test_case} {ans}")