def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    a = {}
    for i in range(len(name)):
        a[name[i]] = yearning[i]
    
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in a:
                answer[i] += a[photo[i][j]]
    return answer

name = input().split()
yearning = list(map(int, input().split()))
photo = list()
for _ in range(3):
    photo.append(input().split())

print(solution(name, yearning, photo))