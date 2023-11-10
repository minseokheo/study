def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int("".join(map(str, lst))))
        return
    
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int("".join(map(str, lst)))*10 + n
            if chk not in v:
                dfs(n+1)
                v.append(chk)
            
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for test_case in range(1, T+1):
    st, t = input().split()
    N = int(t)
    lst = []
    for ch in st:
        lst.append(int(ch))
    L = len(st)
    ans = 0
    v = []
    dfs(0)
    print(f"#{test_case} {ans}")