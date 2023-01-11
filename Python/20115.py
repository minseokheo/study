N = int(input())
energy_drink = list(map(int ,input().split()))

energy_drink.sort()
sum = 0

for i in energy_drink:
  sum = sum + i / 2

print(sum + energy_drink[-1] / 2)