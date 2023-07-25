import math
def solution(fees, records):
    answer = []
    precord = {}
    crecord = {}
    outrecord = []
    inout = []
    
    for record in records:
        words = record.split(" ")
        if words[2] == "IN":
            precord[words[1]] = list(map(int, words[0].split(":")))
            inout.append(words[1])
        else:
            inout.remove(words[1])
            outrecord = list(map(int, words[0].split(":")))
            if outrecord[1] < precord[words[1]][1]:
                outrecord[0] -= 1
                outrecord[1] += 60
            if words[1] not in crecord:
                crecord[words[1]] = (outrecord[0]-precord[words[1]][0])*60 + (outrecord[1]-precord[words[1]][1])
            else:
                crecord[words[1]] += (outrecord[0]-precord[words[1]][0])*60 + (outrecord[1]-precord[words[1]][1])
    
    if len(inout) != 0:
        for i in inout:
            if i not in crecord:
                crecord[i] = (23-precord[i][0])*60 + (59-precord[i][1])
            else:
                crecord[i] += (23-precord[i][0])*60 + (59-precord[i][1])
    
    for k, v in crecord.items():
        if v > fees[0]:
            crecord[k] = fees[1] + math.ceil((v-fees[0])/fees[2])*fees[3]
        else:
            crecord[k] = fees[1]
    crecord = sorted(crecord.items(), key = lambda x : x[0])
    for i in range(len(crecord)):
        answer.append(crecord[i][1])
    return answer