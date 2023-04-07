import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = list()

def avg(nlist):
  return round(sum(nlist) / len(nlist))

def mid(nlist):
  nlist.sort()
  return nlist[len(nlist)//2]

def many_num(nlist):
  num_list = Counter(nlist).most_common(2)
  
  if len(num_list) > 1 and num_list[0][1] == num_list[1][1]:
    return num_list[1][0]
  else:
    return num_list[0][0]

def num_range(nlist):
  return max(nlist) - min(nlist)

for i in range(N):
  num_list.append(int(sys.stdin.readline()))

print(avg(num_list))
print(mid(num_list))
print(many_num(num_list))
print(num_range(num_list))