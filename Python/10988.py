def pallindrom(word):
  for i in range(len(word)//2):
    if word[i] != word[-(i+1)]:
      return 0
  
  return 1


word = list(input())

print(pallindrom(word))