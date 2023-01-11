hour, minute = map(int, input().split())

if minute < 45:
  minute = minute + 15
  if hour < 1:
    hour = 23
  else:
    hour = hour - 1
else:
  minute = minute - 45

print(hour, minute)