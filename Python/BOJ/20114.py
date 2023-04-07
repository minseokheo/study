N, H, W = map(int, input().split())

result = list()

for i in range(N):
  result.append('?')

for i in range(H):
  in_list = list(input())
  for j in range(len(in_list)):
    if in_list[j] != '?':
      index = j // W
      if result[index] != '?':
        continue 
      result[index] = in_list[j]

str_result = ''.join(result)

print(str_result)