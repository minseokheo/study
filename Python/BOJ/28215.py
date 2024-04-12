from itertools import combinations

N, K = map(int, input().split())
points = list()

for _ in range(N):
    points.append(list(map(int, input().split())))

max_near_dist = list()

for combi in combinations(points, K):
    loca = list(combi)
    near_dist = list()
    for point in points:
        dist = list()
        for i in range(K):
            dist.append(abs(point[0]-loca[i][0]) + abs(point[1]-loca[i][1]))
        near_dist.append(min(dist))
    max_near_dist.append(max(near_dist))

print(min(max_near_dist))