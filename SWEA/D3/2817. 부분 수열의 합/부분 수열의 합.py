T = int(input())

def dfs(n, sm):
    global ans
    if K < sm:
        return
    if n == N:
        if sm == K:
            ans += 1
        return

    dfs(n+1, sm+num_list[n])
    dfs(n+1, sm)

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print(f"#{test_case} {ans}")