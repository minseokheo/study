n = int(input())
perfect_num = list()
sum = 0

while n != -1:
  for i in range(1, n):
    if n % i == 0:
      perfect_num.append(i)

  for j in perfect_num:
    sum += j
  
  if sum != n:
    print("{} is NOT perfect.".format(n))
  else:
    print("{} = ".format(n), end='')

    for k in range(len(perfect_num)):
      if k != len(perfect_num)-1:
        print("{} + ".format(perfect_num[k]), end='')
      else:
        print("{}".format(perfect_num[k]))
  n = int(input())
  sum = 0
  perfect_num.clear()