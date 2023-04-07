T = int(input())

for i in range(T):
  N, K = list(map(int, input().split()))
  dist = 0
  direct = 1
  count = 1
  start = 0
  end = 0
  ch_direct = False # True가 R False가 L
  
  while True:
    start = K * count * direct 
    dist += start - end
    direct *= -1

    if dist >= N:
      dist -= start - end
      ch_direct = True
      break

    end = K * count * direct
    dist += start - end
    direct *= -1

    if dist >= N:
      dist -= start - end
      ch_direct = False
      break

    count += 1
  
  if ch_direct == False:
    print("{} L".format(start-(N-dist-1)))
  else:
    print("{} R".format(end+(N-dist-1)))