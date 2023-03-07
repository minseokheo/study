import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
wrong = list(map(int, input().split()))

count = abs(100 - N)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
      if int(nums[j]) in wrong:
        break
      elif j == len(nums)-1:
         count = min(count, abs(int(nums) - N) + len(nums))

print(count)