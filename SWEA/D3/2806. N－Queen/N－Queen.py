T = int(input())

def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

for test_case in range(1, T+1):
    N = int(input())
    v1 = [0] * (2 * N)
    v2 = [0] * (2 * N)
    v3 = [0] * (2 * N)
    ans = 0
    dfs(0)

    print(f"#{test_case} {ans}")