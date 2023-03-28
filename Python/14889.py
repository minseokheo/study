from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    S[i] = list(map(int, input().split()))
start_team = list()
diff = sys.maxsize

def back_tracking(start, cnt):
    global diff
    if cnt == N//2:
        link_team = list()
        for i in range(N):
            if i not in start_team:
                link_team.append(i)

        start_combi = list(combinations(start_team, 2))
        link_combi = list(combinations(link_team, 2))
        s_sum = 0
        l_sum = 0

        for i in range(len(start_combi)):
            s_sum += S[start_combi[i][0]][start_combi[i][1]] + S[start_combi[i][1]][start_combi[i][0]]
            l_sum += S[link_combi[i][0]][link_combi[i][1]] + S[link_combi[i][1]][link_combi[i][0]]
        
        diff = min(diff, abs(s_sum-l_sum))

        return
    
    for i in range(start, N):
        start_team.append(i)
        back_tracking(i+1, cnt+1)
        start_team.pop()
    
back_tracking(0, 0)
print(diff)