import sys
input = sys.stdin.readline

S = input()
newS = list()
sum = 0

for i in range(len(S)-1):
    if 'A' <= S[i] <= 'Z':
        newS.append(S[i])
    else:
        sum += int(S[i])
        
newS.sort()
result = ''.join(newS) + str(sum)
print(result)