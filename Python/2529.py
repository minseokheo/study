import sys
input = sys.stdin.readline

k = int(input())
a = list(map(str, input().split()))
visited = [0] * 10
max_ans = -1
min_ans = sys.maxsize
tmp = list()

def back_tracking(cnt):
    global max_ans, min_ans

    if len(tmp) == k+1:
        num = int(''.join(map(str, tmp)))
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
        return
    
    for i in range(10):
        if visited[i] == 0:
            if cnt == 0:
                tmp.append(i)
                visited[i] = 1
                back_tracking(cnt+1)
                tmp.pop()
                visited[i] = 0
            else:
                if a[cnt-1] == '<':
                    if tmp[cnt-1] < i:
                        tmp.append(i)
                        visited[i] = 1
                        back_tracking(cnt+1)
                        tmp.pop()
                        visited[i] = 0
                else:
                    if tmp[cnt-1] > i:
                        tmp.append(i)
                        visited[i] = 1
                        back_tracking(cnt+1)
                        tmp.pop()
                        visited[i] = 0

back_tracking(0)

if max_ans < 10**k:
    max_ans = '0' + str(max_ans)

if min_ans < 10**k:
    min_ans = '0' + str(min_ans)
    
print(max_ans)
print(min_ans)