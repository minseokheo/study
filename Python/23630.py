N = int(input())
A = list(map(int, input().split()))

bit_calc = [0] * 32

def calc_bit(num):
  temp = num
  n = 0
  while temp > 0:
    bit_calc[n] = bit_calc[n] + (temp % 2)
    temp = temp // 2
    n += 1


for num in A:
  calc_bit(num)

print(max(bit_calc))