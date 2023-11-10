T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    ans = -1
    for R in range(1, N+1):
        C = 1
        while R*C <= N:
            value = A*abs(R-C) + B*abs(N-R*C)
            if ans == -1:
                ans = value
            else:
                ans = min(ans, value)
            C += 1
    print(f"#{test_case} {ans}")