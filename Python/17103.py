import sys
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]
m = max(nums)

prime_numbers = [False, False] + [True] * (m-1)

for i in range(2, int(m**0.5)+1):
  if prime_numbers[i]:
    for j in range(i+i, m+1, i):
      if prime_numbers[j]:
        prime_numbers[j] = False

for num in nums:
  count = 0

  for i in range((num//2)+1):
    if prime_numbers[i] and prime_numbers[num-i]:
      count += 1
  
  print(count)