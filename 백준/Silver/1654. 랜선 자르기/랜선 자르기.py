import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan_cable = list()

for _ in range(K):
    lan_cable.append(int(input()))

start = 1
end = max(lan_cable)

while start <= end:
    mid = (start+end)//2
    count = 0

    for cable in lan_cable:
        count += cable // mid
    
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)