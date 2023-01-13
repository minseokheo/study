import sys

def recursion(s, l, r, count):
  if l >= r: return 1, count
  elif s[l] != s[r]: return 0, count
  else: 
    count += 1
    return recursion(s, l+1, r-1, count)

def isPalindrome(s, count):
  return recursion(s, 0, len(s)-1, count)

T = int(sys.stdin.readline())

for i in range(T):
  count = 1
  word = sys.stdin.readline().rstrip()
  pal_count, re_count = isPalindrome(word, count)
  print(pal_count, re_count)