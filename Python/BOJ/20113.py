N = int(input())
vote = list(map(int, input().split()))
vote_dict = {}
max_list = list()

for i in vote:
  if i == 0:
    continue
  if vote_dict.get(i) is None:
    vote_dict[i] = 1
  else:
    vote_dict[i] += 1

if not vote_dict:
  print("skipped")
else:
  most = max(vote_dict.values())

  for key, value in vote_dict.items():
    if value == most:
      max_list.append(key)

  if len(max_list) == 1:
    print(max_list[0])
  else:
    print("skipped")