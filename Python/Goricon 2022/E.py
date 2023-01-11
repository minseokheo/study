B = int(input())
low = [[0 for j in range(50)] for i in range(B)]
high = [[0 for j in range(50)] for i in range(B)]

for k in range(B):
  low[k] = input()

for l in range(B):
  high[l] = input()

N = int(input())
low_count = 0
high_count = 0
ltemp = ""
htemp = ""

for case in range(N):
  data = list(input())
  for d in data:
    ltemp += d
    htemp += d

    for i in range(B):
      if low[i] in ltemp:
        low_count += 1
        ltemp = ltemp[1:]
        # for change in range(len(ltemp)):
        #   if ltemp[change] == '0' or ltemp[change] == '1':
        #     ltemp[change] = '2'
        #     break
    
    for j in range(B):
      if high[j] in htemp:
        high_count += 1
        htemp = htemp[1:]
        # for ch in range(len(htemp)):
        #   if htemp[ch] == '0' or htemp[ch] == '1':
        #     htemp[ch] = '2'
        #     break
  
  print(low_count)
  print(high_count)

  if low_count < high_count:
    print("LOW {}".format(high_count - low_count))
  else:
    print("HIGH {}".format(low_count - high_count))