S = list(map(int, input().split()))
E = list(map(int, input().split()))

Sdays = S[0] * 360 + S[1] * 30 + S[2]
Edays = E[0] * 360 + E[1] * 30 + E[2]

days = Edays - Sdays

year_v = 0

year = days // 360

for i in range(year):
    A = i // 2
    year_v = year_v + 15 + A

if days // 30 >= 36:
  month_v = 36
else:
  month_v = days // 30

print(year_v, month_v)
print("{}days".format(days))